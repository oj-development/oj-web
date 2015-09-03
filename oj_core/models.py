from django.db import models
from .proglang import proglang
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=100)
    background = models.TextField(blank=True)
    description = models.TextField(blank=True)
    input = models.TextField(blank=True)
    output = models.TextField(blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)
    time_limitation = models.TextField(blank=True)
    hint = models.TextField(blank=True)
    source = models.TextField(blank=True)
    submit=models.PositiveIntegerField(default=0)
    ac=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    __repr__ = __str__
    class Meta:
        ordering = ['name']
        unique_together = ("name", "description")

class Data(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    data_hash = models.CharField(max_length=32)
    def __str__(self):
        try:
            return self.problem.name+" ("+self.data_hash+")"
        except Exception as e:
            return "* ("+self.data_hash+")"
    __repr__ = __str__
    class Meta:
        verbose_name = 'datum'
        verbose_name_plural = 'data'
        ordering = ['problem']
        
class UserStatus(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    submit=models.PositiveIntegerField(default=0)
    ac=models.PositiveIntegerField(default=0)
    submit_problems=models.PositiveIntegerField(default=0)
    ac_problems=models.PositiveIntegerField(default=0)
    solved_problems=models.ManyToManyField(Problem, related_name='solved_by')
    tried_problems=models.ManyToManyField(Problem, related_name='tried_by')
    def get_name(self):
        try:
            return User.objects.get(pk=self.user_id).username
        except Exception as e:
            return "Non-exist user"
    def get_nickname(self):
        try:
            return User.objects.get(pk=self.user_id).first_name
        except Exception as e:
            return ""
    def __str__(self):
        return self.get_name()+" ("+str(self.user_id)+")"
    __repr__ = __str__
    class Meta:
        verbose_name_plural = 'user statuses'
        ordering = ['user_id']
    
class Status(models.Model):
    runid=models.UUIDField()
    user=models.ForeignKey(UserStatus, on_delete=models.SET_NULL, null=True)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    score=models.PositiveSmallIntegerField(default=0)
    result=models.PositiveSmallIntegerField(default=10)
    memory=models.PositiveIntegerField(default=0)
    time=models.FloatField(default=0)
    language=models.CharField(max_length=7, choices=proglang)
    code=models.TextField()
    code_length=models.PositiveIntegerField()
    submit_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.pk)+" - "+str(self.runid)+" ("+str(self.user or "Anonymous")+" / "+str(self.problem)+")"
    __repr__ = __str__
    class Meta:
        verbose_name_plural = 'statuses'
        ordering = ['-submit_time']