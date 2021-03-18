from django.shortcuts import render


def index(request):
    """Главная страница.
    """


    return render(
        request,
        'main/index.html',
        {
            # 'prod': prod,
        }
    )