from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

#Нужно для простой проверки, ввел ли пользователь телефон или нет. 
#смотрит на количество цифр, цифры ли это, и с чего начинается номер
def validate_phone_numbers(phone_number):
    try:
        number_check = int(phone_number)
        try:
            if phone_number[0] == '+' or phone_number[0] == 8:
                if len(phone_number) == 11 or len(phone_number) ==12:
                    return phone_number
        except ValidationError:
            return 'You made a mistake, please check your number again'
    except ValueError:
        return 'This is not a real number'