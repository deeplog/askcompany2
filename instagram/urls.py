from django.urls import path, re_path

from . import views

class YearConverter:
    regex =r"20\d{2}"

    def to_python(self, value):
        return int(value) #view 함수 호출되기전에 인자를 한번 정리

    def to_url(self, value):
        return str(value) #url 리버스할때 URL 문자열로 변환

urlpatterns =[
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    re_path('archives/(?P<year>\d{4})/', views.archives_year)
    # re_path(r'(?P<pk>\d+)/$', views.post_detail())
]