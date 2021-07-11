from django.db import models

# Create your models here.

class report(models.Model):
    # 周报填写人
    report_name = models.CharField('汇报人', max_length=20)
    # # 周报日期
    report_date = models.DateField('周报日期')
    # 周报redflag
    report_redflag = models.CharField(max_length=200)
    report_achievements = models.CharField(max_length=1000)
    report_supportNeeded = models.CharField(max_length=100)



