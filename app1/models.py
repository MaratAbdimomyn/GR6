from django.db import models

class Weekdays(models.Model):
    w_name = models.CharField(max_length=50)
    w_number = models.IntegerField()
    
    def week_day(self):
        return self.w_name