from django.db.models import CharField, ManyToManyField, CheckConstraint, EmailField, Q
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Length

from users.validators import MinLenUsernameValidator, RegexpStringValidator
from api import conf

CharField.register_lookup(Length)


class CustomUserModel(AbstractUser):
    email = EmailField(unique=True,
                       verbose_name='Email',
                       max_length=conf.MAX_LEN_EMAIL_FIELD,
                       help_text=conf.USERS_HELP_EMAIL)
    username = CharField(
        max_length=conf.MAX_LEN_USERS_CHARFIELD,
        unique=True,
        verbose_name='Имя пользователя',
        help_text=(conf.USERS_HELP_UNAME,),
        validators=(
            MinLenUsernameValidator(min_len=conf.MIN_USERNAME_LENGTH),
            RegexpStringValidator()
        ),
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=conf.MAX_LEN_USERS_CHARFIELD,
        help_text=conf.USERS_HELP_FNAME

    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=conf.MAX_LEN_USERS_CHARFIELD,
        help_text=conf.USERS_HELP_FNAME
    )
    password = CharField(
        verbose_name='Пароль',
        max_length=conf.MAX_LEN_USERS_CHARFIELD,
    )
    subscribe = ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False
    )

    def __str__(self):
        return f'{self.username}: {self.email}'

    class Meta:
        verbose_name = 'Пользователь',
        verbose_name_plural = 'Пользователи',
        ordering = ('username',)
        constraints = (
            CheckConstraint(
                check=Q(username__length__gte=conf.MIN_USERNAME_LENGTH),
                name='\nusername to longest\n',
            ),
        )
