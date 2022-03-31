from django.shortcuts import redirect, render

# models 
from .models import users

# database
import mysql.connector

# pagination
from django.core.paginator import Paginator


# Create your views here.

def header(request):
    return render(request, 'header.html')


def footer(request):
    return render(request, 'footer.html')


def contact(request):
    return render(request, 'contact.html')


def work(request):
    return render(request, 'work.html')


def client(request):
    data = users.objects.all()
    pages = Paginator(data, 2)
    page_no = request.GET.get('page')
    print("page_no ", page_no)
    final_data = pages.get_page(page_no)
    totalpage = final_data.paginator.num_pages
    totarange = range(1, totalpage+1)
    print("count ", totalpage)
    context = {'data': final_data,
               'totalpage': totalpage,
               "totarange": totarange}
    return render(request, 'client.html', context)


def about(request):
    return render(request, 'about.html')


def home(request):

    return render(request, 'home.html')


def singin(request):
    mylist = {
        'rec2': '',
        'rec1': '',
        'value1': '',
        'bank_name': 'sbi',
        'account_no': '0987654321',
        'vehicale': '4-wheeler',
        'owner_name': '',
        'phone_no': '',
        'email':''
    }
    contexts = {
        'context': mylist,
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="WEBUSER"
        )
        mycursor = mydb.cursor()
        sql = "SELECT EXISTS(SELECT * FROM mylpi_users WHERE username=%s AND password=%s)"
        data_tupl = (username, password)
        mycursor.execute(sql, data_tupl)
        myresult = mycursor.fetchall()
        print(myresult)
        if myresult[0][0] is not 0:
            sql = "SELECT * FROM mylpi_users WHERE username=%s AND password=%s"
            data_tupl = (username, password)
            mycursor.execute(sql, data_tupl)
            myresult = mycursor.fetchall()
            mylist['owner_name']=myresult[0][1]
            mylist['email']=myresult[0][2]
            mylist['phone_no']=myresult[0][5]
            print(myresult)
            print(mylist)
            print("login succ")
            return redirect('/', mylist)
        else:
            print("not login failed")
    return render(request, 'singin.html')


def singup(request):
    if request.method == 'POST':
        data = users()
        print("data ", data)
        data.username = request.POST.get('username')
        data.email = request.POST.get('email')
        data.dateofbirth = request.POST.get('dateofbirth')
        data.phoneno = request.POST.get('phoneno')
        data.country = request.POST.get('country')
        data.password = request.POST.get('password')
        data.save()
        print("data added succ")
        return redirect('/singin')
    return render(request, 'singup.html')
