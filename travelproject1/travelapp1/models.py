from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
from django.db import models

# Create your models here.
class place(models.Model):

    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics1')
    desc=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class news(models.Model):

    names=models.CharField(max_length=100)
    cate = models.CharField(max_length=200)
    imgs=models.ImageField(upload_to='pics1')
    des=models.CharField(max_length=300)
    def __str__(self):
        return self.names



