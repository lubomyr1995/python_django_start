import os
from uuid import uuid1


def upload_car_to(instance, file: str, ) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.auto_park.user.email, 'cars', f'{uuid1()}.{ext}')
