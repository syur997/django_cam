from django.db import models
# db에는 생성하지 않음, 공통으로 적용되는 모델틀을 생성
class CommonModel(models.Model):
    '''common model Definition'''

    # object가 처음 생성된 시간
    created = models.DateTimeField(auto_now_add=True, null=True)
    # 업데이트되는 시간
    updated = models.DateTimeField(auto_now=True)

    # db에 저장x 설정
    class Meta:
        abstract = True

# Create your models here.
