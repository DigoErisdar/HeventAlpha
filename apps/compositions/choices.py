SOLIDER = 'soldier'
CAPTAIN = 'captain'
MAJOR = 'major'
MARSHAL = 'marshal'
MASTER = 'master'

RANK_CHOICES = (
    (SOLIDER, 'Рядовой'),
    (CAPTAIN, 'Капитан'),
    (MAJOR, 'Майор'),
    (MARSHAL, 'Маршал'),
    (MASTER, 'Мастер'),
)


WAIT = 'wait'
CONFIRM = 'confirm'
CANCEL = 'cancel'

REQUEST_CHOICES = (
    (WAIT, 'Ожидание'),
    (CONFIRM, 'Принят'),
    (CANCEL, 'Отклонено')
)

ENTER = 'enter'
LEFT = 'left'

ACTION_CHOICES = [
    ('Гильдия', (
            (ENTER, 'Вступил в гильдию'),
            (LEFT, 'Покинул гильдию'),
        )
    ),
]