from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class Sub(models.Model):
    SELECTIONS = (
        ("Option A", "Option A"),
        ("Option B", "Option B"),
        ("Option C", "Option C"),
        ("Option D", "Option D")
    )
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    slug = models.SlugField(max_length = 250)
    question_1 = models.CharField(max_length = 100, default = '')
    question_2 = models.CharField(max_length = 100, default = '')
    question_3 = models.CharField(max_length = 100, default = '')
    question_4 = MultiSelectField(choices = SELECTIONS, default = '')
