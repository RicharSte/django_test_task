from django import forms

from .models import Book_info

class BookForm(forms.ModelForm):
    #выводим все поля кроме владельца, оно должно ставиться автоматицески
    class Meta:
        model = Book_info
        fields = [
            'title',
            'descriptiom',
            'prise',
            'condition',
            'image'
        ]
