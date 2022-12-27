from django.urls import path, re_path

from . import views
urlpatterns =[
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    path('archives/<int:year>/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail())
]