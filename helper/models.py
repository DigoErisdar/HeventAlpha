import hashlib
import random

from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode


def P(*kwargs):
    for obj in kwargs:
        print(obj, type(obj), dir(obj), sep="\n")


def get_slug(title):
    """
    Создает слаг по строке
    :param title: строка
    :return: слаг
    """
    return slugify(unidecode(title))


def upload_image(cls, field, filename, obj=None):
    """
    Ссылка для сохранения изображений
    :param apps: __file__
    :param cls: self
    :param field: field
    :param obj: obj has slug and pk
    :param filename: filename
    :return: path
    """
    if filename is not False:
        app = cls.__module__.split('.')[1]
        model = cls.__class__.__name__
        path = ['images', app, model, field]
        if obj:
            path.append(str(obj))
        if hasattr(cls, 'slug'):
            extension = filename.split('.')[-1]
            filename = f"{cls.slug}.{extension}"
        path.append(filename)
        return '/'.join(path)


def __create_token():
    return hashlib.pbkdf2_hmac(hash_name='sha256',
                               password=bytes(str(random.randint(0, 9999999999999)), encoding='utf-8'),
                               salt=bytes(settings.SECRET_KEY, encoding='utf-8'),
                               iterations=45672).hex()


def get_unique_token(field='slug', model=None, obj=None) -> str:
    if model is None and obj is None:
        raise ValueError("Укажи model или obj")
    model = model or obj.__class__
    token = __create_token()
    while model.objects.filter(**{field: token}).exists():
        token = __create_token()
    return token
