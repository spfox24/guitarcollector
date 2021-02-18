from django.db import models
from django.urls import reverse
from datetime import date

SESSIONS = (
    ('THEORY', 'Theory'),
    ('SCALES', 'Scales'),
    ('ARPEGGIOS', 'Arpeggios'),
    ('CHORDS', 'Chords'),
    ('COMPOSITION', 'Composition'),
)

TIME = (
    ('20', '20 minutes'),
    ('30', '30 minutes'),
    ('45', '45 minutes'),
    ('60', '60 minutes'),
)

class Case(models.Model):
    case = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('cases_detail', kwargs={'case_id': self.id})

class Guitar(models.Model):
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    serial = models.CharField(max_length=250)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    cases = models.ManyToManyField(Case)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('guitars_detail', kwargs={'guitar_id': self.id})

    def practiced_for_today(self):
        return self.practice_set.filter(date=date.today()).count() >= 1

class Practice(models.Model):
    date = models.DateField('Practice Date')
    time = models.CharField(
        max_length=2,
        choices=TIME,
        default=TIME[0][0],
    )
    focus = models.CharField(
        max_length=50,
        choices=SESSIONS,
        default=SESSIONS[0][0]
    )

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_focus_display()} on {self.date} for {self.get_time_display()}"

    class Meta:
        ordering: ['-date']


