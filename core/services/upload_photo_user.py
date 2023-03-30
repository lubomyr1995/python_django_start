import os
from uuid import uuid1


def upload_user_photo(instance, file: str):
    ext = file.split('.')[-1]
    return os.path.join(instance.user.email, 'avatars', f'{uuid1()}.{ext}')
