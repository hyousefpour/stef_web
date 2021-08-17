from django.shortcuts import render, get_object_or_404
from .models import (
    Body_News_Notifications,
    Body_site_data_box,
    Body_site_dataManage_box,
    Body_site_data_links,
    Body_site_data_Address,
)


def Body_Home_View(request):
    context = {
        "Body_News": Body_News_Notifications.objects.filter(status="v", managerAccept="t"),
        "DatManage": Body_site_dataManage_box.objects.filter(status="v", managerAccept="t"),
        "DatStef": Body_site_data_box.objects.filter(status="v", managerAccept="t"),
        "DatLink": Body_site_data_links.objects.filter(status="v"),
        "DatAddress": Body_site_data_Address.objects.filter(status="v"),
    }
    return render(request, "main_page/home.html", context)


def detail(request, slug):
    context = {
        "DataNews": get_object_or_404(Body_News_Notifications.objects.filter(status="v", managerAccept="t"), slug=slug),
    }
    return render(request, "main_page/detail.html", context)

# def detail(request, slug):
    # context = {
    #     # "article": get_object_or_404(Article, slug=slug, status="p"),
    #     "article": get_object_or_404(Article.objects.published(), slug=slug),
    # }
    # return render(request, "blog/detail.html", context)
