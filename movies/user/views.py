from django.shortcuts import render
def register(request):
    '''
    注册页
    ：parm request
    :return:
    '''
    return render(request,'register.html')
    