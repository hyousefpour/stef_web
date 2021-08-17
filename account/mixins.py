from django.http import Http404
from django.shortcuts import get_object_or_404
from main_page.models import (
        Body_News_Notifications,
        Body_site_data_box,
        Body_site_data_links,
        Body_site_data_Address,
    )


class FiedsMixin:
    def __init__(self):
        self.fields = ["title", "slug", "content", "thumbnail", "publish", "status"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:  # فقط ادمین اجازه اصلاح وضعیت مقاله را داشته باشد
            self.fields.append("author")
            self.fields.append("managerAccept")
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def __init__(self):
        self.request = None

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status == 'n':  # اگر کاربر وضعیت مقاله در هنگام ارسال مشخص نکرد بطور اتوماتیک پیش نویس باشد
                self.obj.status = 'n'
        return super().form_valid(form)


class BodyNewsAccessMixin:  # در اینجا اجاره دسترسی به مقالات را به خود نویسنده می دهد نه به کاربران دیگر
    def dispatch(self, request, pk, *args, **kwargs):
        BodyNews = get_object_or_404(Body_News_Notifications, pk=pk)  # در اینجا مقاله را می گیرد
        if BodyNews.author == request.user and BodyNews.managerAccept in ['nt'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را ببینید")


class SuperUserAccessMixin:  # کلاس حذف اطلاعات
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را ببینید")


class BodyDataAccessMixin:  # در اینجا اجاره دسترسی به مقالات را به خود نویسنده می دهد نه به کاربران دیگر
    def dispatch(self, request, pk, *args, **kwargs):
        BodyData = get_object_or_404(Body_site_data_box, pk=pk)  # در اینجا مقاله را می گیرد
        if BodyData.author == request.user and BodyData.managerAccept in ['nt'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را ببینید")


class FiedsMixinData:
    def __init__(self):
        self.fields = ["title", "slug", "content", "publish", "status"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:  # فقط ادمین اجازه اصلاح وضعیت مقاله را داشته باشد
            self.fields.append("author")
            self.fields.append("managerAccept")
        return super().dispatch(request, *args, **kwargs)


# Address Link Site
class FiedsMixinLink:
    def __init__(self):
        self.fields = ["title", "slug", "address", "publish", "status"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:  # فقط ادمین اجازه اصلاح وضعیت مقاله را داشته باشد
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)


class LinkSiteAccessMixin:  # در اینجا اجاره دسترسی به مقالات را به خود نویسنده می دهد نه به کاربران دیگر
    def dispatch(self, request, pk, *args, **kwargs):
        BodyNews = get_object_or_404(Body_site_data_links, pk=pk)  # در اینجا مقاله را می گیرد
        if BodyNews.author == request.user in ['n'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را ببینید")


# Address Sandogh
class FiedsMixinAddress:
    def __init__(self):
        self.fields = ["title", "slug", "content", "publish", "status"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request, *args, **kwargs)


class AddressAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        BodyNews = get_object_or_404(Body_site_data_Address, pk=pk)  # در اینجا مقاله را می گیرد
        if BodyNews.author == request.user in ['n'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما نمی توانید این صفحه را ببینید")
