from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BookForm

#оцень похоже на пове для получения информации от юзера
#тут тоже нужно пускать  зарегистрированных пользователей
@login_required(login_url='/login/')
def get_book_info(request, *args, **kwargs):
    if request.method == 'POST':
        #дополнительный параметр позволяет загрузить фото (я про request.FILES)
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            info = form.save(commit=False)
            #показываем зависимость в явном виде
            info.owner = request.user
            info.save()
            return redirect('home')

    else:
        form = BookForm(request.POST or None)
    
    return render(request,'books\Book-info.html', {'form':form})

