from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, User_InfoForm

#Нужно для отображение базовой страницы
def index(request, *args, **kwargs):
    if request.user.is_authenticated:
        context = {
            'page_title': "It's working",
            'username': request.user.username
        }
    else:
        context = {
                'page_title': "It's working"
            }
    return render(request,'index.html', context)

#простая форма логина
def loginPage(request):
    #принимаем значения форма и смотрим, корректно ли они заполнены
    form = LoginForm(request.POST or None)
    if form.is_valid:
        if request.method == 'POST':
            #получаем логин и пароль для входа в систему
            username = request.POST.get('username')
            password = request.POST.get('password')
            #пытаемся аутенфицироваться
            user = authenticate(username=username, password=password)
            #Проверяем уддачно ли прошла аутенфитикация и логинимся
            if user is not None:
                login(request, user)
                return redirect('home')
    context= {
        'form': form
    }
    return render(request, 'user\login.html', context)

#Функция для заполнения данных о пользователи, дальше будет нужна для созддания фида
#нужно допускать к ней только залогинившихся пользователей
@login_required(login_url='/login/')
def get_user_info(request):
    #так же как и в логине
    if request.method == 'POST':
        form = User_InfoForm(request.POST or None)
        if form.is_valid():
            #поскольку нам нужно показать связанность с таблицей User мы не сохраняем данные и показываем связь в явном виде
            info = form.save(commit=False)
            #устанавливаем зависимость
            info.user = request.user
            #сохраняем
            info.save()
            return redirect('home')

    else:
        form = User_InfoForm(request.POST or None)
    
    return render(request,'user\get-info.html', {'form':form})
