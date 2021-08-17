from django.db import models


# class prs_code(models.Model):
#     username = models.IntegerField(unique=True, null=False, primary_key=True, verbose_name="کدکاربری")
#     password = models.CharField(max_length=100, null=False, verbose_name="رمز ورود")
#     firstname = models.CharField(max_length=70, null=True, verbose_name="نام")
#     lastname = models.CharField(max_length=70, null=True, verbose_name="نام خانوادگی")
#     meli_code = models.CharField(max_length=20, verbose_name="کدملی")
#     mobil = models.CharField(max_length=50, null=True, verbose_name='شماره تلفن همراه')
#     email = models.EmailField(verbose_name="ایمیل")
#
#     class Meta:
#         verbose_name = "عضوصندوق"
#         verbose_name_plural = "اعضاء صندوق"
#         ordering = ['lastname', 'firstname']
#
#     def __str__(self):
#         return self.lastname
class User(models.Model):
    username = models.IntegerField(unique=True, null=False, primary_key=True, verbose_name="کدکاربری")
    password = models.CharField(max_length=100, null=False, verbose_name="رمز ورود")
    firstname = models.CharField(max_length=70, null=True, verbose_name="نام")
    lastname = models.CharField(max_length=70, null=True, verbose_name="نام خانوادگی")
    meli_code = models.CharField(max_length=20, verbose_name="کدملی")
    mobil = models.CharField(max_length=50, null=True, verbose_name='شماره تلفن همراه')
    email = models.EmailField(verbose_name="ایمیل")

    class Meta:
        verbose_name = "عضوصندوق"
        verbose_name_plural = "اعضاء صندوق"
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return self.lastname


class last_case_prs(models.Model):
    personel_code = models.IntegerField(null=True, verbose_name='کدپرسنلی')
    bank = models.CharField(max_length=70, null=True, verbose_name='نام بانک')
    no_hesab = models.CharField(max_length=70, null=True, verbose_name='شماره حساب')
    ando_total = models.IntegerField(null=True, verbose_name='جمع سرمایه')
    ando_installment = models.IntegerField(null=True, verbose_name='مبلغ قسط سرمایه')
    due = models.IntegerField(null=True, verbose_name='مانده بدهی')
    vam_installment = models.IntegerField(null=True, verbose_name='مبلغ قسط وام')
    return_pay_92 = models.IntegerField(null=True, verbose_name='برگشت سود سهام سال 92')
    return_pay_96 = models.IntegerField(null=True, verbose_name='برگشت سود سهام سال 96')
    return_pay_98 = models.IntegerField(null=True, verbose_name='برگشت سود سهام سال 98')

    class Meta:
        verbose_name = "آخرین وضعیت عضو"
        verbose_name_plural = "آخرین وضعیت اعضا"
        ordering = ['personel_code']

    def __str__(self):
        return self.personel_code


class data_vam_conferment(models.Model):
    keyconf = models.BigIntegerField(unique=True, null=True, verbose_name="کد")
    radif = models.IntegerField(null=True, verbose_name='ردیف')
    personel_code = models.IntegerField(null=True, verbose_name='کدپرسنلی')
    loan_type = models.CharField(max_length=70, null=True, verbose_name='نوع وام')
    loan_account = models.IntegerField(null=True, verbose_name='مبلغ وام')
    numberof_instalment = models.IntegerField(null=True, verbose_name='تعداد قسط')
    instalment_account = models.IntegerField(null=True, verbose_name='مبلغ قسط')
    pricework_wage = models.IntegerField(null=True, verbose_name='مبلغ كارمزد')
    insurance_amount = models.IntegerField(null=True, verbose_name='مبلغ بيمه')
    payable_account = models.IntegerField(null=True, verbose_name='مبلغ خالص پرداختي وام')
    payment_date = models.IntegerField(null=True, verbose_name='تاريخ پرداخت')

    class Meta:
        verbose_name = 'شرح وام پرداختی'
        verbose_name_plural = "شرح وام های پرداختی"
        ordering = ['keyconf']

    def __str__(self):
        return self.keyconf


class data_ando(models.Model):
    personel_code = models.IntegerField(null=True, verbose_name='کدپرسنلی')
    payment_date = models.IntegerField(null=True, verbose_name='تاريخ پرداخت')
    description = models.CharField(max_length=70, null=True, verbose_name='شرح واريزي')
    pay_amount = models.IntegerField(null=True, verbose_name='مبلغ واريزي')
    capital_add = models.IntegerField(null=True, verbose_name='جمع واريزي')
    variz_type = models.CharField(max_length=70, null=True, verbose_name='نحوه واريزي')

    class Meta:
        verbose_name = "پرداخت قسط اندوخته "
        verbose_name_plural = "پرداخت قسط اندوخته ها"
        ordering = ['payment_date']

    def __str__(self):
        return self.payment_date


class d_vam(models.Model):
    personel_code = models.IntegerField(null=True, verbose_name='کدپرسنلی')
    payment_date = models.IntegerField(null=True, verbose_name='تاريخ پرداخت')
    description = models.CharField(max_length=70, null=True, verbose_name='شرح واريزي')
    pay_amount = models.IntegerField(null=True, verbose_name='مبلغ قسط وام')
    due_remaining = models.IntegerField(null=True, verbose_name='مانده بدهي')
    variz_type = models.CharField(max_length=70, null=True, verbose_name='نحوه واريزي')

    class Meta:
        verbose_name = "پرداخت قسط وام "
        verbose_name_plural = "پرداخت قسط وام ها"
        ordering = ['payment_date']

    def __str__(self):
        return self.payment_date

    # def get_absolute_url(self):
    #     return reverse("account:news")
