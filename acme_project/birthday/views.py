# birthday/views.py
from django.shortcuts import render

# Импортируем класс BirthdayForm, чтобы создать экземпляр формы.
from .forms import BirthdayForm
from .utils import calculate_birthday_countdown


def birthday(request):
    form = BirthdayForm(request.GET or None)
    # если объект request.GET пуст — срабатывает условиe or и форма создаётся
    # без параметров, через BirthdayForm(None).

    # Создаём словарь контекста сразу после инициализации формы.
    context = {'form': form}

    if form.is_valid():
        birthday_countdown = calculate_birthday_countdown(
            # ...и передаём в неё дату из словаря cleaned_data.
            form.cleaned_data['birthday']
        )
        # Обновляем словарь контекста: добавляем в него новый элемент.
        context.update({'birthday_countdown': birthday_countdown})

    # Передаём форму в словарь контекста:
    # Добавляем его в словарь контекста под ключом form:
    # Указываем нужный шаблон и передаём в него словарь контекста.
    return render(request, 'birthday/birthday.html', context)