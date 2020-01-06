from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from APP.models import User


def hello(request):
    return HttpResponse('hello')


def login(request):
    if request.method=="GET":
        return render(request,'login.html')

    elif request.method=="POST":
        username =request.POST.get("username")
        password = request.POST.get("password")

        users = User.objects.filter(username = username)
        if users.exists():
            user = users.first()
            if user.password == password:
                # user.state = 1
                request.session["username"] = username
                # user.save()
                return render(request, 'classify.html', context={'user':user})
            else:
                return render(request, 'login.html', context={"message": 'no'})
        else:
            return render(request,'login.html',context={"message":'no'})

def logout(request):
    request.session.flush()
    return render(request,'index.html')



def register(request):
    if request.method=="GET":
        return render(request,'register.html')

    elif request.method=="POST":
        username =request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        user = User()
        user.username = username
        user.password = password
        user.email = email
        user.save()
        return render(request,"register_success.html")

# def check_user(request):
#     username = request.GET.get("username")
#     users = User.objects.filter(username = username)
#
#     data = {
#         "exist":0
#     }
#     if users.exists():
#         data["exist"] = 1
#     else:
#         pass
#     return JsonResponse(data = data)

# 这个是分类classify的页面，写错名字了


def show_index(request):
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        return render(request, 'classify.html',context={'user':user})
    else:
        return render(request, 'classify.html')

def index(request):
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        return render(request, 'index.html',context={'user':user})
    else:
        return render(request, 'index.html')