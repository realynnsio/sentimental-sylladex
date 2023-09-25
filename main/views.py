from django.shortcuts import render, redirect
from main.models import Item
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    context = {
        'app_name': 'The Sentimental Sylladex',
        'name': request.user.username,
        'pbp_class' : 'PBP E',
        'last_login': request.COOKIES['last_login'],
    }

    items = Item.objects.filter(user=request.user) # changed .values()
    amounts = Item.objects.filter(user=request.user).values_list('amount')
    amount_total = 0
    for amount in amounts:
        amount_total += int(amount[0])
    
    context['amount_total'] = amount_total
    context['items'] = items

    return render(request, "main.html", context)

def create_item(request):
    context = { 'app_name': 'The Sentimental Sylladex' }

    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context['form'] = form
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# def adjust_amount(request, id, num):
#     data = Item.objects.filter(pk=id)

#     if ((data.amount + num) <= 0):
#         data.delete()
#     else:
#         data.amount += num
#         data.save()

#     return redirect('main:main')
#     # is this right idk what else to do