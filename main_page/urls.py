from django.urls import path
from .views import Body_Home_View, detail

app_name = "MainPage"
urlpatterns = [
    path('', Body_Home_View, name='BodyView'),
    path('DataNews/<slug:slug>', detail, name='detail'),
]


# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
