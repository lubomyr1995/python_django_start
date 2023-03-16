from rest_framework.views import APIView
from rest_framework.response import Response
import json
from typing import TypedDict

FILENAME = 'users.json'
User = TypedDict('User', {'id': int, 'name': str, 'age': int})


def read_file(file_name=FILENAME):
    with open(file_name) as file:
        users = json.load(file)
        return users


def write_to_file(data, file_name=FILENAME):
    with open(file_name, 'w') as file:
        json.dump(data, file)


class UserLiltCreateView(APIView):
    def get(self, *args, **kwargs):
        try:
            users = read_file()
            return Response(users)
        except Exception as err:
            Response({'error': str(err)})

    def post(self, *args, **kwargs):
        try:
            users: list[User] = read_file()
            user_id = users[-1]['id'] + 1 if users else 1
            data: User = self.request.data
            data.update(id=user_id)
            users.append(data)
            write_to_file(users)
            return Response(data)
        except Exception as err:
            Response({'error': str(err)})


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        try:
            user_id = kwargs.get('pk')
            users: list[User] = read_file()
            user = next(filter(lambda i: i['id'] == user_id, users))
            print(user)
            if not user:
                Response('Not found')
            return Response(user)

        except Exception as err:
            Response({'error': str(err)})

    def put(self, *args, **kwargs):
        try:
            user_id = kwargs.get('pk')
            users: list[User] = read_file()
            data = self.request.data
            index = next((index for index, value in enumerate(users) if value["id"] == user_id), None)
            if not index:
                return Response('Not Found')
            users[index] = {'id': user_id, **data}
            write_to_file(users)
            return Response({'id': user_id, **data})
        except Exception as err:
            Response({'error': str(err)})

    def patch(self, *args, **kwargs):
        try:
            user_id = kwargs.get('pk')
            users: list[User] = read_file()
            data = self.request.data
            user = next(filter(lambda item: item['id'] == user_id, users), None)
            # user = None
            # for item in users:
            #     if item['id'] == user_id:
            #         user = item
            #         break
            if not user:
                return Response('Not Found')
            user |= {**data}
            write_to_file(users)
            return Response(user)
        except Exception as err:
            Response({'error': str(err)})

    def delete(self, *args, **kwargs):
        try:
            user_id = kwargs.get('pk')
            users: list[User] = read_file()
            index = next((index for index, value in enumerate(users) if value['id'] == user_id), None)
            if not index:
                return Response('Not Found')
            del users[index]
            write_to_file(users)
            return Response('deleted')
        except Exception as err:
            Response({'error': str(err)})
