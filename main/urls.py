from django.urls import path
from main.views import show_main, create_item, show_html, show_json, show_json_by_id, show_xml, show_xml_by_id
from main.views import register, login_user, logout_user, adjust_amount, decrease_amount, delete_item
from main.views import get_item_json, create_ajax
from main.views import create_product_flutter, show_json_by_user, show_json_by_username

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('html', show_html, name='show_html'),
    path('xml', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json-by-user/', show_json_by_user, name='show_json_by_user'),
    path('json-by-username/<str:username>/', show_json_by_username, name='show_json_by_username'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('adjust-amount/<int:id>/<int:num>/', adjust_amount, name='adjust_amount'),
    path('decrease-amount/<int:id>/<int:num>/', decrease_amount, name='decrease_amount'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
