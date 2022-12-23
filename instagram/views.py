from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q','') # 키가 없을때는 ''
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q':q, #input type에 전달
    })