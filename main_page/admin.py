from django.contrib import admin
from .models import (
    Body_News_Notifications,
    Body_site_data_box,
    Body_site_dataManage_box,
    Body_site_data_links,
    Body_site_data_Address,
)

admin.site.site_header = "صندوق تعاونی اعتبار فرهنگیان "


class Body_News_Notifications_admin(admin.ModelAdmin):
    list_display = ('title', 'jpublish', 'status', 'slug', 'managerAccept')
    list_filter = ('publish', 'status', 'title')
    search_fields = ('title', 'managerAccept')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Body_News_Notifications, Body_News_Notifications_admin)


class Body_site_data_box_admin(admin.ModelAdmin):
    list_display = ('title', 'jpublish', 'status', 'managerAccept')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Body_site_data_box, Body_site_data_box_admin)


class Body_site_dataManage_box_admin(admin.ModelAdmin):
    list_display = ('title', 'jpublish', 'status', 'managerAccept')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Body_site_dataManage_box, Body_site_dataManage_box_admin)


class Body_site_data_links_admin(admin.ModelAdmin):
    list_display = ('title', 'jpublish', 'status')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Body_site_data_links, Body_site_data_links_admin)


class Body_site_data_Address_admin(admin.ModelAdmin):
    list_display = ('title', 'jpublish', 'status')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Body_site_data_Address, Body_site_data_Address_admin)
