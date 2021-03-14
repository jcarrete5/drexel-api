# Generated by Django 3.1.7 on 2021-03-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("crn", models.CharField(max_length=5)),
                ("course_num", models.CharField(max_length=4)),
                ("subject_code", models.CharField(max_length=4)),
                ("description", models.TextField()),
                ("credits", models.DecimalField(decimal_places=2, max_digits=3)),
                (
                    "corequisites",
                    models.ManyToManyField(
                        related_name="_course_corequisites_+", to="courses.Course"
                    ),
                ),
                (
                    "prerequisites",
                    models.ManyToManyField(
                        related_name="dependents", to="courses.Course"
                    ),
                ),
            ],
        ),
    ]