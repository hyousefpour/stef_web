import MySQLdb
import xlrd
from .models import User, last_case_prs, data_vam_conferment, data_ando, d_vam
from django.shortcuts import render, redirect, HttpResponse


# from .forms import ProfileForm


def getdata(request):
    #  **************** send_data_site.mdb ******************
    prsdb = MySQLdb.connect(host="localhost", user="root", database="datastef")
    cur_mysql = prsdb.cursor()

    # *************  prs.mdb ***************
    sql = "DELETE FROM prsuser_User"
    cur_mysql.execute(sql)
    prsdb.commit()

    query = "INSERT INTO prsuser_User(username, password, firstname, lastname, meli_code, mobil) VALUES (%s, %s, %s, %s, %s, %s)"
    book = xlrd.open_workbook("D:/send_data_web/prs.xls")
    sheet = book.sheet_by_name("prs")

    for row in range(1, sheet.nrows):
        username = sheet.cell(row, 0).value
        password = sheet.cell(row, 1).value
        firstname = sheet.cell(row, 2).value
        lastname = sheet.cell(row, 3).value
        melicode = sheet.cell(row, 4).value
        mobil = sheet.cell(row, 5).value

        valu = (
            username, password.encode('utf8'), firstname.encode('utf8'), lastname.encode('utf8'),
            melicode.encode('utf8'), mobil.encode('utf8'))
        cur_mysql.execute(query, valu)
    prsdb.commit()

    # *************  last_case_prs.mdb ***************
    sql = "DELETE FROM prsuser_last_case_prs"
    cur_mysql.execute(sql)
    prsdb.commit()

    query = "INSERT INTO prsuser_last_case_prs(personel_code, bank, no_hesab, ando_total, ando_installment, due, vam_installment, return_pay_92, return_pay_96, return_pay_98) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    book = xlrd.open_workbook("D:/send_data_web/last_case_prs.xls")
    sheet = book.sheet_by_name("last_case_prs")

    for row in range(1, sheet.nrows):
        personel_code = sheet.cell(row, 0).value
        bank = sheet.cell(row, 1).value
        nohesab = sheet.cell(row, 2).value
        andototal = sheet.cell(row, 3).value
        andoinstallment = sheet.cell(row, 4).value
        due = sheet.cell(row, 5).value
        vaminstallment = sheet.cell(row, 6).value
        returnpay92 = sheet.cell(row, 7).value
        returnpay96 = sheet.cell(row, 8).value
        returnpay98 = sheet.cell(row, 9).value

        valu = (personel_code, bank.encode('utf8'), nohesab.encode('utf8'), andototal, andoinstallment, due,
                vaminstallment, returnpay92, returnpay96, returnpay98)
        cur_mysql.execute(query, valu)
    prsdb.commit()

    # # **********  d_vam_conferment  *************
    sqlconf = "DELETE FROM prsuser_data_vam_conferment"
    cur_mysql.execute(sqlconf)
    prsdb.commit()

    queryconf = "INSERT INTO prsuser_data_vam_conferment(keyconf, radif, personel_code, loan_type, loan_account, numberof_instalment, instalment_account, pricework_wage, insurance_amount, payable_account, payment_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    conf = xlrd.open_workbook("D:/send_data_web/data_vam_conferment.xls")
    sheet = conf.sheet_by_name("data_vam_conferment")

    for row in range(1, sheet.nrows):
        keyconf = sheet.cell(row, 0).value
        radif = sheet.cell(row, 1).value
        personelcode = sheet.cell(row, 2).value
        loantype = sheet.cell(row, 3).value
        loanaccount = sheet.cell(row, 4).value
        numberofinstalment = sheet.cell(row, 5).value
        instalmentaccount = sheet.cell(row, 6).value
        priceworkwage = sheet.cell(row, 7).value
        insuranceamount = sheet.cell(row, 8).value
        payableaccount = sheet.cell(row, 9).value
        paymentdate = sheet.cell(row, 10).value

        valconf = (
            keyconf, radif, personelcode, loantype.encode('utf8'), loanaccount, numberofinstalment, instalmentaccount,
            priceworkwage, insuranceamount, payableaccount, paymentdate)
        cur_mysql.execute(queryconf, valconf)

    prsdb.commit()

    # #  **************** data_ando.mdb ******************
    sqlando = "DELETE FROM prsuser_data_ando"
    cur_mysql.execute(sqlando)
    prsdb.commit()

    queryando = "INSERT INTO prsuser_data_ando(personel_code, payment_date, description, pay_amount, capital_add, variz_type) VALUES (%s, %s, %s, %s, %s, %s)"
    ando = xlrd.open_workbook("D:/send_data_web/data_ando.xls")
    sheet = ando.sheet_by_name("data_ando")

    for row in range(1, sheet.nrows):
        personel_code = sheet.cell(row, 0).value
        payment_date = sheet.cell(row, 1).value
        description = sheet.cell(row, 2).value
        pay_amount = sheet.cell(row, 3).value
        capital_add = sheet.cell(row, 4).value
        variz_type = sheet.cell(row, 5).value

        valando = (
            personel_code, payment_date, description.encode('utf8'), pay_amount, capital_add, variz_type.encode('utf8'))
        cur_mysql.execute(queryando, valando)
    prsdb.commit()

    # #  **************** data_vam.mdb ******************
    sqlvam = "DELETE FROM prsuser_d_vam"
    cur_mysql.execute(sqlvam)
    prsdb.commit()

    queryando = "INSERT INTO prsuser_d_vam(personel_code, payment_date, description, pay_amount, due_remaining, variz_type) VALUES (%s, %s, %s, %s, %s, %s)"
    vam = xlrd.open_workbook("D:/send_data_web/d_vam.xls")
    sheet = vam.sheet_by_name("d_vam")

    for row in range(1, sheet.nrows):
        personel_code = sheet.cell(row, 0).value
        payment_date = sheet.cell(row, 1).value
        description = sheet.cell(row, 2).value
        pay_amount = sheet.cell(row, 3).value
        due_remaining = sheet.cell(row, 4).value
        variz_type = sheet.cell(row, 5).value

        valvam = (
            personel_code, payment_date, description.encode('utf8'), pay_amount, due_remaining,
            variz_type.encode('utf8'))
        cur_mysql.execute(queryando, valvam)
    prsdb.commit()

    prsdb.close()

    return render(request, "prsuser/getdatabank.html")


# =======================================================
# loginprs
def Loginprs(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('data_prs:profileprs')
        else:
            return HttpResponse(
                '<h1 style="text-align: center; background-color: red; color: white; height: 50px; width: 600px">!!!لطفا نام کاربری یا رمز عبور معتبر وارد کنید </h1>')

    return render(request, 'prsuser/loginprs.html')


# Profileprs
def Profileprs(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {
            'prsdata': User.objects.filter(username=current_user)
        }
        return render(request, 'prsuser/Profileprs.html', context)

    else:
        return redirect('login')


# logout_prs
def logoutprs(request):
    return render(request, 'prsuser/logout_prs.html')


# last case prs
def lastcaseprs(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {
            'lastcase': last_case_prs.objects.filter(personel_code=current_user)
        }
        return render(request, 'prsuser/lastcaseprs.html', context)


# data_vam_conferment
def datavamconf(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {
            'conf': data_vam_conferment.objects.filter(personel_code=current_user)
        }
        return render(request, 'prsuser/datavamconf.html', context)


# data_ando
def dataando(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {
            'ando': data_ando.objects.filter(personel_code=current_user)
        }
        return render(request, 'prsuser/dataando.html', context)


# d_vam
def dvam(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {
            'vam': d_vam.objects.filter(personel_code=current_user)
        }
        return render(request, 'prsuser/datavam.html', context)
