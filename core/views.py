from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('<h1>"Изучаем django"</h1><strong>Автор</strong>: <i>Ралдугина Е. С.</i>')

def about(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Page</title>
    </head>
    <body>
        <p>Имя: Евгения</p>
        <p>Отчество: Станиславовна</p>
        <p>Фамилия: Ралдугина</p>
        <p>Телефон: 8-921-633-26-19</p>
        <p>Email: evgeniya_raldugina@vk.com</p>
    </body>
    </html>
    """
    return HttpResponse(html)

# Глобальная переменная с товарами
items = [
    {"id": 1, "name": "Кроссовки abibas"},
    {"id": 2, "name": "Куртка кожаная"},
    {"id": 3, "name": "Coca-cola 1 литр"},
    {"id": 4, "name": "Картофель фри"},
    {"id": 5, "name": "Кепка"},
    {"id": 6, "name": "Стол"},
    {"id": 7, "name": "Стул"},
    {"id": 8, "name": "Фотоаппарат"},
    {"id": 9, "name": "Лампа"},
    {"id": 10, "name": "Шкаф"},
]

def item(request, id):

    item = next((item for item in items if item["id"] == id), None)

    
    if id == 10 and item is None:
        return HttpResponse(f'Товар "Шкаф" не найден<br><a href="/items/">Назад к списку товаров</a>')

    if item:
        return render(request, 'core/item.html', {'item': item})
    else:

        return HttpResponse(f'Товар с id={id} не найден<br><a href="/items/">Назад к списку товаров</a>')

def items_list(request):

    return render(request, 'core/items_list.html', {'items': items})