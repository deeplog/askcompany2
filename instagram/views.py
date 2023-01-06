from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

#post_list = ListView.as_view(model=Post, paginate_by=10)

@login_required
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

#
# def post_detail(request: HttpRequest, pk) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post':post,
#         }
#     )

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset = Post.objects.filter(is_public = True))

class PostDetailView(DetailView):
    model = Post
    #queryset = Post.objects.`filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()

def archives_year(request, year):
    return HttpResponse(f"{year}년 Archives")