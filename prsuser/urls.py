from django.urls import path
from .views import (
    getdata,
    Loginprs,
    Profileprs,
    logoutprs,
    lastcaseprs,
    datavamconf,
    dataando,
    dvam
)

app_name = 'data_prs'
urlpatterns = [
    path('getdata/', getdata, name='getdate'),
    path('Loginprs/', Loginprs, name='loginprs'),
    path('profileprs/', Profileprs, name='profileprs'),
    path('logoutprs/', logoutprs, name='logoutprs'),
    path('lastcaseprs/', lastcaseprs, name='lastcaseprs'),
    path('conf/', datavamconf, name='conf'),
    path('ando/', dataando, name='ando'),
    path('vam/', dvam, name='vam'),
]
