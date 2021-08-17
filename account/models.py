from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):  # (Abstract = چکیده  author= نویسنده  special= خاص   staff= کارکنان)
    is_author = models.BooleanField(default=False, verbose_name="وضعیت نویسنده")
    special_user = models.DateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")

    def is_special_user(self):  # برای وضعیت فعال یا غیرفعال بودن کاربر ویژه در باز زمانی مشخص شده
        if self.special_user > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True  # برای اینکه به شکل یک آیکون ضربدر نشان داده شود
    is_special_user.short_description = "وضعیت کاربر ویژه"  # (description = شرح)
