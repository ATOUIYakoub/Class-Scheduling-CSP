from django.db import models

class TimetableSlot(models.Model):
    DAY_CHOICES = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
    ]

    TIME_SLOT_CHOICES = [
        ('08.30 to 10.00', '08.30 to 10.00'),
        ('10.10 to 11.40', '10.10 to 11.40'),
        ('11.50 to 13.20', '11.50 to 13.20'),
        ('13.30 to 15.00', '13.30 to 15.00'),
        ('15.10 to 16.40', '15.10 to 16.40'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.CharField(max_length=30, choices=TIME_SLOT_CHOICES)
    module_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    classroom_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.module_name} - {self.teacher_name} - {self.day} {self.start_time}"

