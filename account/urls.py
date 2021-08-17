from django.contrib.auth import views
from django.urls import path
from .views import (
    BodyNewsList,
    BodyNewsCreate,
    BodyNewsUpdate,
    BodyNewsDelete,
    DataBoxList,
    DataBoxUpdate,
    DataManagerList,
    DataManagerUpdate,
    LinkSiteList,
    LinkSiteCreate,
    LinkSiteUpdate,
    LinkSiteDelete,
    AddressList,
    AddressUpdate,
    Profile,
    Login,
    PasswordChange,
)


app_name = 'account'
urlpatterns = [
    # path('login/', views.LoginView.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    #
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', BodyNewsList.as_view(), name="news"),
    path('bodynews/create/', BodyNewsCreate.as_view(), name='BodyNews-create'),
    path('bodynews/update/<int:pk>', BodyNewsUpdate.as_view(), name='BodyNews-update'),
    path('bodynews/delete/<int:pk>', BodyNewsDelete.as_view(), name='BodyNews-delete'),
    path('DataBoxList/', DataBoxList.as_view(), name="DataBoxList"),
    path('BodyData/update/<int:pk>', DataBoxUpdate.as_view(), name="DataBoxUpdate"),
    # path('BodyData/update/', DataBoxUpdate.as_view(), name="DataBoxUpdate"),
    path('DataManagerList/', DataManagerList.as_view(), name="DataManagerList"),
    path('BodyManager/update/<int:pk>', DataManagerUpdate.as_view(), name="DataManagerUpdate"),
    path('LinkList', LinkSiteList.as_view(), name="LinkList"),
    path('LinkList/create/', LinkSiteCreate.as_view(), name='LinkListCreate'),
    path('LinkList/update/<int:pk>', LinkSiteUpdate.as_view(), name='LinkListUpdate'),
    path('LinkList/delete/<int:pk>', LinkSiteDelete.as_view(), name='LinkListDelete'),
    path('AddressList/', AddressList.as_view(), name="AddressSandogh"),
    path('AddressSandogh/update/<int:pk>', AddressUpdate.as_view(), name="AddressUpdate"),
    path('profile/', Profile.as_view(), name='profile'),
]

