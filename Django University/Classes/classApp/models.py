from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField(max_length=None)
    Instructor_Name = models.CharField(max_length=100)
    Duration = models.FloatField()

    class Meta:
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.Title
