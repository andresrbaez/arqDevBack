from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    short_description = models.TextField(blank=True, null=True)
    modeling = models.CharField(max_length=255, blank=True, null=True)
    planimetry = models.CharField(max_length=255, blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    software = models.CharField(max_length=255, blank=True, null=True)
    vegetation = models.CharField(max_length=255, blank=True, null=True)
    posproduction = models.CharField(max_length=255, blank=True, null=True)
    type_project = models.CharField(max_length=255, null=True, blank=True)
    description_subtitle = models.CharField(max_length=200, null=True, blank=True)
    description_1 = models.TextField(null=True, blank=True)
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    description_4 = models.TextField(null=True, blank=True)
    description_5 = models.JSONField(default=dict, null=True, blank=True)
    description_6 = models.JSONField(default=dict, null=True, blank=True)
    media = models.JSONField(default=dict, null=True, blank=True)
    
    def __str__(self):
        return self.title

    # Para eliminar permamentemente los datos de algún proyecto
    def delete(self, using=None, keep_parents=False):
        self.media.storage.delete(self.media.name)
        super().delete()