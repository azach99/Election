
from django.db import models
from multiselectfield import MultiSelectField
from PNAM.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

class Subs(models.Model):
    SELECTIONS_4 = (
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
        ("Candidate E", "Candidate E"),
        ("Candidate F", "Candidate F"),
        ("Candidate G", "Candidate G"),
        ("Candidate 1", "Candidate 1"),
        ("Candidate 2", "Candidate 2"),
        ("Candidate 3", "Candidate 3"),
        ("Candidate 4", "Candidate 4"),
        ("Candidate 5", "Candidate 5")
    )
    SELECTIONS = (
        ("Choose", "Choose"),
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
    )
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    slug = models.SlugField(max_length = 250)
    random_key = models.CharField(max_length = 250, blank = True)
    admin_email = models.EmailField(max_length = 100, default = 'admin_user@gmail.com')
    phone_number = models.CharField(max_length = 200, default = '')
    question_1 = models.CharField(max_length = 100, default = '', choices = SELECTIONS)
    question_2 = models.CharField(max_length = 100, default = '', choices = SELECTIONS)
    question_3 = models.CharField(max_length = 100, default = '', choices = SELECTIONS)
    question_4 = MultiSelectField(choices = SELECTIONS_4, default = '')
    question_5 = MultiSelectField(choices = SELECTIONS_4, default = '')
    question_6 = models.CharField(max_length=100, default='', choices=SELECTIONS)
    question_7 = models.CharField(max_length=100, default='', choices=SELECTIONS)
    question_8 = models.CharField(max_length=100, default='', choices=SELECTIONS)
    question_9 = models.CharField(max_length=100, default='', choices=SELECTIONS)
    question_10 = models.CharField(max_length=100, default='', choices=SELECTIONS)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender = Subs)