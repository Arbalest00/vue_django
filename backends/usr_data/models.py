from django.db import models
class usr_data(models.Model):
    device_id = models.CharField(max_length=100,unique=True)
    x = models.FloatField()
    y = models.FloatField()
    altitude = models.FloatField()
    speed_x = models.FloatField()
    speed_y = models.FloatField()
    speed_z = models.FloatField()
    posture = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'usr_data'
        