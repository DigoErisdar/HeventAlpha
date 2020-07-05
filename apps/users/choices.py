FIELDS = {
    'name': 'Имя',
    'date_birthday': 'День рождение',
    'gender': 'Пол',
}
FIELD_CHOICES = (tuple(FIELDS.items()))


ALL = 'all'
SOKLAN = 'soklan'
ADMIN = 'admin'

VALUE_CHOICES = (
    (ALL, 'Всем'),
    (SOKLAN, 'Сокланам'),
    (ADMIN, 'Админам'),
)
