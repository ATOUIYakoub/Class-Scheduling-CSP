from django.db import models
from datetime import datetime,time, timedelta

# Function to generate time slots
def generate_time_slots():
    start_time = time(8, 30)
    slots = []
    for i in range(5):  # 5 sessions per day
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=90)).time()
        slots.append((start_time.strftime("%H:%M"), f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"))
        start_time = (datetime.combine(datetime.today(), end_time) + timedelta(minutes=10)).time()
    return slots

# Generate the time slot choices
TIME_SLOTS = generate_time_slots()

class TimetableSlot(models.Model):
    day_choices = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=10, choices=day_choices)
    start_time = models.CharField(max_length=10, choices=TIME_SLOTS)
    module_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    classroom_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.module_name} - {self.teacher_name} - {self.day} {self.start_time}"
