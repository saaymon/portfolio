from django.db import models


class Technology(models.Model):
    technology_name = models.CharField(max_length=50)

    def __str__(self):
        return self.technology_name


class Job(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()
    technology_name = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



