from django.db import models

# Create your models here.
class Bundle(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
class Module(models.Model):
    bundle = models.ForeignKey(Bundle)
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class FileType(models.Model):
    name = models.CharField(max_length=50)
    suffix = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name
    
class Files(models.Model):
    module = models.ForeignKey(Module)
    type = models.ForeignKey(FileType)
    name = models.CharField(max_length=100)
    path = models.URLField()
    
    def __unicode__(self):
        return self.name

    
    
