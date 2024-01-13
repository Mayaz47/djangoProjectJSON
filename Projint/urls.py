from django.urls import path
from .views import chart,index2, delete,update

urlpatterns = [
    path('', chart, name='chart'),
    path('index2/', index2, name='page2'),
    path('delete/', delete, name='delete'),
    path('update/', update, name='update')

]
