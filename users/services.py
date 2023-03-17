import json
from typing import TypedDict

User = TypedDict('User', {'id': int, 'name': str, 'age': int})


class UserService:
    __file_name = 'users_db.json'
    __users: list[User] = []

    @classmethod
    def _read_file(cls) -> None:
        try:
            with open(cls.__file_name) as file:
                cls.__users = json.load(file)
        except (Exception,):
            pass

    @classmethod
    def __write_file(cls) -> None:
        with open(cls.__file_name, 'w') as file:
            json.dump(cls.__users, file)

    @classmethod
    def get_all(cls) -> list:
        return cls.__users

    @classmethod
    def add(cls, data: dict) -> User:
        user_id = cls.__users[-1]['id'] + 1 if len(cls.__users) else 1
        # new_user = {**data, 'id': user_id}
        # cls.__users.append(new_user)
        data.update(id=user_id)
        cls.__users.append(data)
        cls.__write_file()
        return data

    @classmethod
    def get_by_id(cls, pk: int) -> User:
        find_user = next((item for item in cls.__users if item['id'] == pk), 'User not found')
        return find_user

    # @classmethod
    # def update_by_id(cls, pk: int, data: dict) -> User | str:
    #     user: dict = cls.get_by_id(pk)
    #
    #     if isinstance(user, str):
    #         return user
    #
    #     user.clear()
    #     user |= {**data, 'id': pk}
    #     cls.__write_file()
    #     return user

    @classmethod
    def update_by_id_all(cls, pk: int, data: dict) -> User | str:
        index = next((i for i, v in enumerate(cls.__users) if v['id'] == pk), None)
        if not index:
            return 'User not found'
        updated_user = {**data, 'id': pk}
        cls.__users[index] = updated_user
        cls.__write_file()
        return updated_user

    @classmethod
    def update_by_id_partial(cls, pk: int, data: dict) -> User | str:
        user = next((item for item in cls.__users if item['id'] == pk), None)
        if not user:
            return 'User not found'
        user |= {**data, 'id': pk}
        cls.__write_file()
        return user

    @classmethod
    def delete_by_id(cls, pk: int) -> str:
        index = next((i for i, v in enumerate(cls.__users) if v['id'] == pk), 'User not found')
        if isinstance(index, str):
            return index
        del cls.__users[index]
        cls.__write_file()
        return 'deleted'
