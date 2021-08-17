from django.contrib import admin
from .models import User, data_vam_conferment, data_ando, d_vam, last_case_prs

admin.site.site_header = "صندوق تعاونی اعتبار فرهنگیان "


class User_admin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'meli_code', 'mobil')
    list_filter = ('lastname', 'firstname')
    search_fields = ('username', 'lastname', 'firstname')


admin.site.register(User, User_admin)


class data_vam_conferment_admin(admin.ModelAdmin):
    list_display = ('keyconf', 'radif', 'personel_code', 'loan_type', 'loan_account', 'payable_account', 'payment_date')


admin.site.register(data_vam_conferment, data_vam_conferment_admin)


admin.site.register(last_case_prs)
# class data_ando_admin(admin.ModelAdmin):
#     list_display = ('personel_code', 'payment_date', 'description', 'pay_amount', 'sattlement_type')
#     # prepopulated_fields = {'slug': ('payment_date',)}
#
#
# admin.site.register(data_ando, data_ando_admin)
admin.site.register(data_ando)

# class d_vam_admin(admin.ModelAdmin):
#     list_display = ('personel_code', 'payment_date', 'description', 'pay_amount', 'due_remaining', 'sattlement_type')
#     # prepopulated_fields = {'slug': ('payment_date',)}
#
#
# admin.site.register(d_vam, d_vam_admin)
admin.site.register(d_vam)
