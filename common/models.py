from django.db import models

class Common(models.Model):
    # auto_now_add : 현재 데이터 생성시간을 기준으로 생성 -> 이후 데이터가 업데이트되어도 수정되지않는다
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now: 생성되는 시간기준으로 일단 생성 -> 이후 업데이트가 되면 시간도 업데이트된 현재시간을 기준으로 업데이트된다
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 데이터베이스의 테이블에 위와 같은 컬럼이 추가되지않는다
