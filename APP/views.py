import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages

from APP.ItemBasedCF import ItemBasedCF
from APP.UserBasedCF1 import UserBasedCF
from APP.models import User, User_movie
from movie.models import Movie_cartoon, Movie_action, Movie_horrible, Movie_comedy, Movie_science, Movie_crime, \
    Movie_love, Movie_story, Movie_all


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
            if user.password == password:
                # user.state = 1
                request.session["username"] = username
                # user.save()
                return render(request, 'index.html', context={'user': user})
            else:
                return render(request, 'login.html', context={"message": 'no'})
        else:
            return render(request, 'login.html', context={"message": 'no'})

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
        return render(request,"login.html",context={'message':'register'})

def check_user(request):
    username = request.POST.get("username")
    users = User.objects.filter(username = username)
    if users.exists():
        return HttpResponse('1')
    else:
        return HttpResponse('0')

# 这个是分类classify的页面，写错名字了


def show_index(request):
    username = request.session.get("username")
    a = list(random.sample(range(1,250),16))
    action_films = Movie_action.objects.filter(id__in = a)
    horrible_films = Movie_horrible.objects.filter(id__in = a)
    comedy_films = Movie_comedy.objects.filter(id__in = a)
    cartoon_films = Movie_cartoon.objects.filter(id__in = a)
    science_films = Movie_science.objects.filter(id__in = a)
    crime_films = Movie_crime.objects.filter(id__in = a)
    love_films = Movie_love.objects.filter(id__in = a)
    story_films = Movie_story.objects.filter(id__in = a)
    if username:
        user = User.objects.filter(username=username).first()
        data = {
            "cartoon_films": cartoon_films,
            'action_films':action_films,
            "horrible_films":horrible_films,
            'comedy_films':comedy_films,
            'science_films':science_films,
            'crime_films':crime_films,
            'love_films':love_films,
            'story_films':story_films,
            'user': user
        }
        return render(request, 'classify.html',context=data)
    else:
        data = {
            "cartoon_films": cartoon_films,
            'action_films':action_films,
            "horrible_films":horrible_films,
            'comedy_films':comedy_films,
            'science_films':science_films,
            'crime_films':crime_films,
            'love_films':love_films,
            'story_films':story_films,
        }
        return render(request, 'classify.html',context=data)

def index(request):
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        return render(request, 'index.html',context={'user':user})
    else:
        return render(request, 'index.html')


def search(request):
    searchtext = request.POST.get('searchtext')
    films = Movie_all.objects.filter(movie_name__contains=searchtext)[0:15]
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        data_on = {
            'films': films,
            'text':searchtext,
            'user': user,
        }
        return render(request,'search_movie.html',context=data_on)
    else:
        data_out ={
            'films': films,
            'text': searchtext,
        }
        return render(request, 'search_movie.html',context=data_out)

def show_movie(request,movie_num):
    films = Movie_all.objects.filter(num = movie_num)
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        data_on = {
            'films': films,
            'user': user
        }
        return render(request,'movie_inf.html',context=data_on)
    else:
        data_out ={
            'films': films,
        }
        # return render(request, 'movie_inf.html',context=data_out)
        return render(request, 'movie_inf.html',context=data_out)

def test(request):
    return HttpResponse('hi')

def tt(request):
    users = User_movie.objects.all()
    return render(request,'test.html',context = {'users':users})

def cti(result):
    a = []
    for i in result:
        i = float(i)
        i = int(i)
        a.append(i)
    return a

def show_recommend(request):
    users = User_movie.objects.all()
    username = request.session.get("username")
    if username:
        user = User.objects.filter(username=username).first()
        userID = int(user.username)
        itemCF = ItemBasedCF()
        itemCF.generate_dataset(users)
        itemCF.calc_movie_sim()
        # itemCF.evaluate()#推荐结果
        result1 = itemCF.recommend(userID)
        result1 = cti(result1)
        first_films = Movie_all.objects.filter(num__in=result1)

        # 第二种
        userCF = UserBasedCF()
        userCF.generate_dataset(users)
        userCF.UserSimilarity()
        print('为该用户推荐的评分最高的10部电影是：'.center(30, '='))
        result2 = userCF.recommend(userID)  # 推荐结果
        result2 = cti(result2)
        second_films = Movie_all.objects.filter(num__in=result2)

        data_on = {
            'first_films': first_films,
            'second_films': second_films,
            'user': user,
        }
        return render(request, 'recommend.html', context=data_on)
    else:
        # data_out = {
        #     'first_films': first_films,
        #     'second_films': second_films,
        # }
        return render(request, 'recommend.html')

def score(request):
    username = request.session.get("username")

    if username:
        user = User.objects.filter(username=username).first()
        movie_num =  request.POST.get('movie_num')
        grade = request.POST.get('scoretext')
        films = Movie_all.objects.filter(num=movie_num)
        um = User_movie.objects.filter(userId=username).filter(movieId = movie_num)
        if um.exists():
            data_on = {
                'films': films,
                'user': user,
            }
            messages.error(request, "已经打过分了")
            return render(request, 'movie_inf.html', context=data_on)
        else:
            u = User_movie()
            u.movieId = movie_num
            u.userId = username
            u.rating = grade
            u.save()
            messages.success(request, "评分成功")
            data_on = {
                'films': films,
                'user': user,
            }
            return render(request, 'movie_inf.html', context=data_on)
    else:
        movie_num = request.POST.get('movie_num')
        films = Movie_all.objects.filter(num=movie_num)
        data_out = {
            'films': films,
        }
        messages.error(request, "请先登陆")
        return render(request, 'movie_inf.html', context=data_out)


def your_score(request):
    username = request.session.get("username")
    user = User.objects.filter(username=username).first()
    ums = User_movie.objects.filter(userId = username).distinct()
    movieids =[i.movieId for i in ums]
    films = Movie_all.objects.filter(num__in=movieids)
    data_on = {
        'user':user,
        'films':films,
    }
    return render(request, 'your_score.html', context=data_on)

def del_score(request):
    return None