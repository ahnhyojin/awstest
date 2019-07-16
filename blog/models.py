from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published', null = True)
    body = models.TextField()
    postHit = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

    def hittingPoint(self):
        self.postHit = self.postHit +1
        self.save()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="comments")  # Post의 pk를 Comment에서 foreignkey로 받아줌(foreignkey 부모의 정보를 갖고오겟다)/ 종속 / 참조 # CASCADE 글을 삭제해도 댓글 데이터는 삭제안됨
       #blog는 부모모델명 첫글짜를 소문자로 써줌(보편적으로) ##related_name ; 하나의 테이블을 만들어준것, 하나의 글에 달린 댓글을 불러올때 쓰이는 이름 
    commentbody = models.TextField()
    commentdate = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.commentbody