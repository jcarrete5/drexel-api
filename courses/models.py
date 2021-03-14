from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    crn = models.CharField(max_length=5)
    course_num = models.CharField(max_length=4)
    subject_code = models.CharField(max_length=4)
    description = models.TextField()
    prerequisites = models.ManyToManyField(
        "self", symmetrical=False, related_name="dependents"
    )
    corequisites = models.ManyToManyField("self", related_name="+")
    credits = models.DecimalField(max_digits=3, decimal_places=2)
