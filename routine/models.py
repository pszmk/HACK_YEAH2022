from django.db import models
from register.models import Users


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)
class Routine(models.Model):
    routine_title = models.CharField(max_length=200)
    routine_description = models.CharField(max_length = 200,null=True,blank=True)
    day = models.CharField(max_length=9,
                  choices=DAYS_OF_WEEK,
                  default="Monday")
    routine_relation=models.ForeignKey('RoutineRelation',related_name='routine_relation',on_delete=models.SET_NULL,null=True,blank=True)  
    user=models.ForeignKey(Users,related_name='related_user',on_delete=models.SET_NULL,null=True,blank=True)   
     
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
  
    def __str__(self):        
        return self.routine_title

class RoutineRelation(models.Model):
    routine_relation_name = models.CharField(max_length=200)
    routine_relation_description = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
       return f'{self.routine_relation_name}'
   
   
