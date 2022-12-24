from django.db import models

class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y%m%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ##return f"Custom Post object({self.id})"
        return self.message

    # admin 단에 구현할 수도 있음
    def message_length(self):
        return len(self.message)
    message_length.short_description = "메세지 글자수" # 화면 출력 글자도 변경


class Comment(models.Model):
    post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE) # post_id 생성
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


