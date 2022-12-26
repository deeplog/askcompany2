from django.views.generic import ListView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Post

post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q','') # 키가 없을때는 ''
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q':q, #input type에 전달
#     })


def post_detail(request: HttpRequest, pk) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World")
    response.write("Hello World")
    response.write("Hello World")
    return response