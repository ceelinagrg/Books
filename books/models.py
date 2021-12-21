from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['pub_date']
    
    def __str__(self):
        return self.name

class HeroInfo(models.Model):
    GENDER_CHOICES=(
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=50)
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    hbook = models.ForeignKey(Book,related_name='heroinfos', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname