from django.db import models

# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length = 20)

    # MEDIA_ROOT 이후의 추가 경로를 설정 => upload_to
    image = models.ImageField(blank=True, upload_to='uploaded')


# 필드 이름	역할	django 필드	속성
# content	내용	Char	max_length=20
# image	이미지	Image	blank=True, upload_to='임의 경로'