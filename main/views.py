from django.shortcuts import render
from main.models import Item

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'The Sentimental Sylladex',
        'name': 'Alma Putri Nashrida',
        'pbp_class' : 'PBP E'
    }

    items = Item.objects.all().values()
    context['items'] = items

    return render(request, "main.html", context)