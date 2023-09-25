from django.urls import path
from main.views import show_main, create_item, show_html, show_json, show_json_by_id, show_xml, show_xml_by_id
from main.views import register, login_user, logout_user, adjust_amount, decrease_amount, delete_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('html', show_html, name='show_html'),
    path('xml', show_xml, name='show_xml'),
    path('json', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('adjust-amount/<int:id>/<int:num>/', adjust_amount, name='adjust_amount'),
    path('decrease-amount/<int:id>/<int:num>/', decrease_amount, name='decrease_amount'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
]
