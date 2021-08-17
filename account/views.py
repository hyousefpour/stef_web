from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
    FiedsMixin,
    FormValidMixin,
    BodyNewsAccessMixin,
    SuperUserAccessMixin,
    FiedsMixinData,
    BodyDataAccessMixin,
    FiedsMixinLink,
    LinkSiteAccessMixin,
    AddressAccessMixin,
    FiedsMixinAddress,
)
from django.urls import reverse_lazy, reverse
from .models import User
from .forms import ProfileForm
from django.contrib.auth.views import PasswordChangeView  # LoginView,
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main_page.models import (
    Body_News_Notifications,
    Body_site_data_box,
    Body_site_dataManage_box,
    Body_site_data_links,
    Body_site_data_Address,
)
from django.contrib.auth.views import LoginView  # , PasswordChangeView


# @login_required()  # این دستور برای نمایش صفحات حتما باید کاربر ورود داشته باشد و هر کاربری نشان نمی دهد
class BodyNewsList(LoginRequiredMixin, ListView):
    template_name = "registration/news.html"
    model = Body_News_Notifications

    def get_queryset(self):
        if self.request.user.is_superuser:  # اگر کاربر مدیر سیستم بود به همه مقالات دسترسی داشته باشد
            return Body_News_Notifications.objects.all()
        else:
            return Body_News_Notifications.objects.filter(author=self.request.user)


class BodyNewsCreate(LoginRequiredMixin, FiedsMixin, FormValidMixin, CreateView):
    model = Body_News_Notifications
    template_name = "registration/CreateUpdateNews.html"


class BodyNewsUpdate(BodyNewsAccessMixin, FiedsMixin, FormValidMixin, UpdateView):
    model = Body_News_Notifications
    template_name = "registration/CreateUpdateNews.html"


class BodyNewsDelete(SuperUserAccessMixin, DeleteView):
    model = Body_News_Notifications
    success_url = reverse_lazy('account:news')
    template_name = "registration/bodynewsdelete.html"


class DataBoxList(LoginRequiredMixin, ListView):
    template_name = "registration/databox.html"

    def get_queryset(self):
        if self.request.user.is_superuser:  # اگر کاربر مدیر سیستم بود به همه مقالات دسترسی داشته باشد
            return Body_site_data_box.objects.all()
        else:
            return Body_site_data_box.objects.filter(author=self.request.user)


class DataBoxUpdate(BodyDataAccessMixin, FiedsMixinData, FormValidMixin, UpdateView):
    model = Body_site_data_box
    template_name = "registration/CreateUpdateDataBox.html"

    def get_success_url(self):
        return reverse('account:DataBoxList')


class DataManagerList(LoginRequiredMixin, ListView):
    template_name = "registration/dataManager.html"

    def get_queryset(self):
        if self.request.user.is_superuser:  # اگر کاربر مدیر سیستم بود به همه مقالات دسترسی داشته باشد
            return Body_site_dataManage_box.objects.all()
        else:
            return Body_site_dataManage_box.objects.filter(author=self.request.user)


class DataManagerUpdate(BodyDataAccessMixin, FiedsMixinData, FormValidMixin, UpdateView):
    model = Body_site_dataManage_box
    template_name = "registration/CreateUpdateDataManager.html"

    def get_success_url(self):
        return reverse('account:DataManagerList')


# Address link site
class LinkSiteList(LoginRequiredMixin, ListView):
    template_name = "registration/LinkList.html"

    def get_queryset(self):
        if self.request.user.is_superuser:  # اگر کاربر مدیر سیستم بود به همه مقالات دسترسی داشته باشد
            return Body_site_data_links.objects.all()
        else:
            return Body_site_data_links.objects.filter(author=self.request.user)


class LinkSiteCreate(LoginRequiredMixin, FiedsMixinLink, FormValidMixin, CreateView):
    model = Body_site_data_links
    template_name = "registration/CreateUpdateLinkList.html"

    def get_absolute_url(self):
        return reverse("account:LinkList")


class LinkSiteUpdate(LinkSiteAccessMixin, FiedsMixinLink, FormValidMixin, UpdateView):
    model = Body_site_data_links
    template_name = "registration/CreateUpdateLinkList.html"

    def get_absolute_url(self):
        return reverse("account:LinkList")


class LinkSiteDelete(SuperUserAccessMixin, DeleteView):
    model = Body_site_data_links
    success_url = reverse_lazy('account:LinkList')
    template_name = "registration/LinkListdelete.html"

    def get_absolute_url(self):
        return reverse("account:LinkList")


# Address Sandogh
class AddressList(LoginRequiredMixin, ListView):
    template_name = "registration/AddressSandogh.html"

    def get_queryset(self):
        if self.request.user.is_superuser:  # اگر کاربر مدیر سیستم بود به همه مقالات دسترسی داشته باشد
            return Body_site_data_Address.objects.all()
        else:
            return Body_site_data_Address.objects.filter(author=self.request.user)


class AddressUpdate(AddressAccessMixin, FiedsMixinAddress, FormValidMixin, UpdateView):
    model = Body_site_data_Address
    template_name = "registration/CreateUpdateAddressSandogh.html"

    def get_success_url(self):
        return reverse('account:AddressSandogh')


# Profile
class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self, queryset=None):  # برای نمایش فقط همان کاربری که وارد سیستم شد
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            # return reverse_lazy("account:home")
            return reverse_lazy("account:profile")
        else:
            return reverse_lazy("account:profile")


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
