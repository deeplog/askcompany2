from django.urls import path, re_path, register_converter

from . import views
from .coverters import YearConverter

register_converter(YearConverter, 'year')

app_name = 'instagram' #URL Reverse에서 namespace 역할을 하게 됨

urlpatterns =[
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    #re_path('archives/(?P<year>\d{4})/', views.archives_year)
    # path('archives/<year:year>/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail())
    path('archive/', views.post_archive, name = 'post_archive'),
    path('archive/<year:year>', views.post_archive_year, name = 'post_year_archive'),
]