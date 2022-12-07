from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

# admin.site.register(Post) # 첫번째 방법

#Post를 admin에 등록하는 세번째 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk','photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] # admin 화면의 보여줄 화면 설정
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # search 옵션 제공

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src ="{post.photo.url}" />')
        return None

    # def message_length(self, post):
    #     return f"{len(post.message)} 글자"
