from django.db import models

# Create your models here.
class Todolist(models.Model):
    task_name=models.CharField(default='',max_length=23)
    created=models.CharField(default='',max_length=40)
    done=models.CharField(default='',max_length=34)
    def __str__(self):
        return self.task_name