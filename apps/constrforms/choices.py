TYPE_FIELD = (
    ('text', 'Текст'),
    ('int', 'Целочисленный'),
    ('choice', 'Выбор'),
    ('img', 'Изображение'),
)

CHOICE_FIELD = {'field': 'Поле', 'radio': 'Радиокнопки'}
MULTICHOICE_FIELD = {'multifield': 'Поле', 'checkbox': 'Чекбокс'}

WIDGET_FIELD = (
    ('Одиночный выбор', tuple(CHOICE_FIELD.items())),
    ('Множественный выбор', tuple(MULTICHOICE_FIELD.items())),
)

REQUEST_ACTION = (
    ('open', 'Открыть'),
    ('close', 'Закрыть'),
)
CHAR_ACTION = (
    ('invite', 'Принять в клан'),
)