from __future__ import unicode_literals
#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime

class Houses(models.Model):
    HID   = models.AutoField(primary_key=True)
    income = models.FloatField(default=0.0)
    point  = models.PointField(default=Point(1,1),null=True)
    def __str__(self):
        return "%s" %(self.HID)

class Members(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    PID=models.AutoField(primary_key=True)
    Age=models.IntegerField(default=0)
    genders=(('M',"Male"),('F',"Female"))
    Name=models.CharField(max_length=30,default="")
    Gender=models.CharField(max_length=1,choices=genders)
    def __str__(self):
        return "%s : %s" %(self.PID,self.Name)



class Farms(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    FID=models.AutoField(primary_key=True)
    plot=models.PolygonField(srid=4326,geography=True)
    area=models.FloatField(default=0.0)
    def __str__(self):
        return "%s" % (self.FID)
    def save(self):
        temp=self.plot.transform(27700,clone=True)
        self.area=temp.area
        super().save(self)

class Crops(models.Model):
    Name=models.CharField(max_length=50,default="Rice")
    FID=models.ForeignKey(Farms,to_field='FID',on_delete=models.CASCADE)
    Year=models.IntegerField()
    seasons=(('S',"Summer"),('W',"Winter"),('M',"Monsoon"))
    Seasons=models.CharField(max_length=20,choices=seasons)
    def __str__(self):
        return "%s : %s" %(self.FID,self.Year)

class Wells(models.Model):
    HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
    WID=models.AutoField(primary_key=True)
    point=models.PointField(default=Point(1,1))
    AvgYield=models.DecimalField(max_digits=7,decimal_places=4)
    def __str__(self):
        return "%s" %(self.WID)

class Yields(models.Model):
    WID=models.ForeignKey(Wells,to_field='WID',on_delete=models.CASCADE)
    Yield=models.FloatField(default=0.0)
    measured_date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return "%s : %s" %(self.WID,self.WID)

# Create your models here.
class Incidences(models.Model):
        #HID=models.ForeignKey(Houses,to_field='HID',on_delete=models.CASCADE)
        #WID=models.AutoField(primary_key=True)
        #point=models.PointField(default=Point(1,1))
        #AvgYield=models.DecimalField(max_digits=7,decimal_places=4)
        #def __str__(self):
        #        return "%s" %(self.WID)
        name = models.CharField(max_length=20)
        location = models.PointField(srid=4326)
        objects = models.GeoManager()

	#def __unicode__(self):
	#	return self.name
        class Meta:
                verbose_name_plural =" Incidences"

class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.counties

    class Meta:
        verbose_name_plural = 'Counties'
    	

