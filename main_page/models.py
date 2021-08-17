from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from extensions.utils import jalali_converter
from account.models import User


# from django.contrib.auth.models import User

class Body_News_Notifications(models.Model):
    STATUS_CHOICES = (
        ('v', 'نمایش'),
        ('n', 'عدم نمایش'),
    )
    STATUS_ACCEPT = (
        ('t', 'تایید'),
        ('nt', 'عدم تایید'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='Body_News',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="عنوان خبر")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس خبر")
    thumbnail = models.ImageField(upload_to="static/images", null=True, blank=True, verbose_name="تصویرخبر")
    # content = RichTextUploadingField(config_name='default', blank=True, verbose_name="محتوا")
    content = models.TextField(verbose_name="محتوا")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='n', verbose_name="وضعیت")
    managerAccept = models.CharField(max_length=2, choices=STATUS_ACCEPT, default='nt', verbose_name="تایید مدیر")

    class Meta:
        verbose_name = "خبر و اطلاعیه"
        verbose_name_plural = "خبرها و اطلاعیه ها"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def get_absolute_url(self):
        return reverse("account:news")

    def thumbnail_tag(self):
        return format_html("<img width=100 height=75 style='border-radius:5ps;' src='{}'".format(self.thumbnail.url))

    thumbnail_tag.short_description = "عکس"


class Body_site_data_box(models.Model):
    STATUS_CHOICES = (
        ('v', 'نمایش'),
        ('n', 'عدم نمایش'),
    )
    STATUS_ACCEPT = (
        ('t', 'تایید'),
        ('nt', 'عدم تایید'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='Body_Data',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name=" اطلاعات صندوق")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    content = models.TextField(verbose_name="محتوا")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="وضعیت")
    managerAccept = models.CharField(max_length=2, choices=STATUS_ACCEPT, verbose_name="تایید مدیر")

    class Meta:
        verbose_name = "اطلاعات صندوق"
        verbose_name_plural = "اطلاعات صندوق"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"


class Body_site_dataManage_box(models.Model):
    STATUS_CHOICES = (
        ('v', 'نمایش'),
        ('n', 'عدم نمایش'),
    )
    STATUS_ACCEPT = (
        ('t', 'تایید'),
        ('nt', 'عدم تایید'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='Body_Manage',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name=" اطلاعات مسئولین")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    content = models.TextField(verbose_name="محتوا")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=1, verbose_name="وضعیت")
    managerAccept = models.CharField(max_length=2, choices=STATUS_ACCEPT, default=1, verbose_name="تایید مدیر")

    class Meta:
        verbose_name = "اطلاعات مسئولین"
        verbose_name_plural = "اطلاعات مسئولین"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def get_absolute_url(self):
        return reverse("account:DataManagerList")


class Body_site_data_links(models.Model):
    STATUS_CHOICES = (
        ('v', 'نمایش'),
        ('n', 'عدم نمایش'),
    )

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='Body_Links',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="لینک ها")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    address = models.CharField(max_length=200, verbose_name="آدرس لینک")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "لینک"
        verbose_name_plural = "لینک ها"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def get_absolute_url(self):
        return reverse("account:LinkList")


class Body_site_data_Address(models.Model):
    STATUS_CHOICES = (
        ('v', 'نمایش'),
        ('n', 'عدم نمایش'),
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='Body_Address',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="آدرس")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس ")
    content = models.TextField(verbose_name="محتوا")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"

    def get_absolute_url(self):
        return reverse("account:AddressSandogh")


from django.core.files.storage import FileSystemStorage
import unicodedata


class ASCIIFileSystemStorage(FileSystemStorage):
    # Convert unicode characters in name to ASCII characters
    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf8')
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
