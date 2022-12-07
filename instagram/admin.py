from django.contrib import admin
from .models import Post

# admin.site.register(Post) # 첫번째 방법

#Post를 admin에 등록하는 세번째 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
