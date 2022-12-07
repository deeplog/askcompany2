from django.contrib import admin
from .models import Post

# admin.site.register(Post) # 첫번째 방법

#Post를 admin에 등록하는 세번째 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'message_length', 'is_public', 'created_at', 'updated_at'] # admin 화면의 보여줄 화면 설정
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # search 옵션 제공

    # def message_length(self, post):
    #     return f"{len(post.message)} 글자"
