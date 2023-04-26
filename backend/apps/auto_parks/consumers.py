import json

from channels.db import database_sync_to_async
from djangochannelsrestframework.decorators import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from .models import AutoParkModel, ChatModel
from .serializers import AutoParkSerializer


class AutoParkConsumer(GenericAsyncAPIConsumer):
    def __init__(self, *args, **kwargs):
        self.room_name = None
        self.name = None
        super().__init__(*args, **kwargs)

    async def connect(self):
        if not self.scope['user']:
            await self.close()

        self.room_name = self.scope['url_route']['kwargs']['room']

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        self.name = await self.get_profile_name()
        await self.accept()

        if self.room_name == 'chat':
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'sender',
                    'message': 'connected to chat',
                    'user': self.name
                }
            )
            messages = await self.get_latest_messages()
            for m in messages:
                await self.send_json({
                    'type': 'sender',
                    'message': m['message'],
                    'user': m['owner']
                })

                # await self.channel_layer.group_send(
                #     self.room_name,
                #     {
                #         'type': 'sender',
                #         'message': m['message'],
                #         'user': m['owner']
                #     }
                # )

    async def sender(self, event):
        await self.send_json(event)

    @action()
    async def send_message(self, data, request_id, action):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'sender',
                'message': data,
                'user': self.name,
                'id': request_id
            }
        )
        await self.save_message_to_db(data, self.scope['user'])

    @model_observer(AutoParkModel, serializer_class=AutoParkSerializer)
    async def auto_park_activity(self, message, action, subscribing_request_ids, **kwargs):
        for request_id in subscribing_request_ids:
            await self.reply(data=message, action=action, request_id=request_id)

    @action()
    async def subscribe_to_auto_park_activity(self, request_id, **kwargs):
        await self.auto_park_activity.subscribe(request_id=request_id)

    @database_sync_to_async
    def get_profile_name(self):
        return self.scope['user'].profile.name

    @database_sync_to_async
    def save_message_to_db(self, message, user):
        ChatModel.objects.create(message=message, owner=user)

    @database_sync_to_async
    def get_latest_messages(self):
        return [{'message': i.message, 'owner': i.owner.profile.name} for i in ChatModel.objects.reverse()[:3]]
