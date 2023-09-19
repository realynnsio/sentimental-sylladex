from django.shortcuts import render
from main.models import Item
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Mengembalikan Data dalam Bentuk XML


# Create your views here.
def show_main(request):
    context = {
        'app_name': 'The Sentimental Sylladex',
        'name': 'Alma Putri Nashrida',
        'pbp_class' : 'PBP E'
    }

    items = Item.objects.all() # changed .values()
    amounts = Item.objects.all().values_list('amount')
    amount_total = 0
    for amount in amounts:
        amount_total += int(amount[0])
    
    context['amount_total'] = amount_total
    context['items'] = items

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_html(request):
    try:
        dataset = Item.objects.all()

        html_render = ""

        for data in dataset:
            html_render += f"""
            <p>Name: {data.name}</p>
            <p>Amount: {data.amount}</p>
            <p>Description: {data.description}</p>
            
            <hr>
            """

        return HttpResponse(html_render)
    
    except Item.DoesNotExist:
        return HttpResponse("There are no items in your Sylladex right now.")

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
