from django.db import models

# Create your models here.
# import한 model의 model을 상속받아옴.
class Blog(models.Model) : 
    title = models.CharField(max_length=200) #charfield : 제한이 있는 문자형 필드
    writer = models.CharField(max_length =100)
    pub_date = models.DateTimeField()
    body = models.TextField() #textfield : 제한이 없는 문자형 필드
    image = models.ImageField(upload_to="blog/", blank=True, null=True)

# class 만들면서 테이블 하나 만들거라하는 명령어들
# python manage.py makemigrations :  테이블을 이렇게 만들거란 걸 migrations라는 폴더에 저장시킴.
# python manage.py migrate : 마이그레이션 폴더를 디져서 db  sql에 적용시킴.

# python manage.py createsuperuser : admin패널을 이용해 디비 확인하기 위해 슈퍼 계정 만드는 명령어

    def __str__(self): #어디선가 객체가 호출될떄의 이름표설정하는 것과 같음.
        return self.title

    def summary(self):
        return self.body[:100]
