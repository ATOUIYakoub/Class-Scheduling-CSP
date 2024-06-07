from datetime import datetime, timedelta
from .models import TimetableSlot

MODULES = [
    'Securite_lecture', 'Securite_td', 'Methodes_formelles_lecture', 'Methodes_formelles_td',
    'Analyse_numerique_lecture', 'Analyse_numerique_td', 'Entrepreneuriat_lecture',
    'Recherche_operationnelle_lecture', 'Recherche_operationnelle_td',
    'Distributed_architecture_lecture', 'Distributed_architecture_td',
    'Reseaux_lecture', 'Reseaux_td', 'Reseaux_tp', 'AI_lecture', 'AI_td', 'AI_tp'
]

TEACHERS = {
    'Mme. Zaidi': ['Reseaux_tp'],
    'Dr. Issadi': ['Recherche_operationnelle_lecture','Recherche_operationnelle_td'],
    'Dr. Zedek': ['Methodes_formelles_lecture', 'Methodes_formelles_td'],
    'Mr. Sahli': ['Reseaux_td'],
    'Mme. Hamma': ['AI_tp'],
    'Dr. Djenadi': ['Distributed_architecture_lecture', 'Distributed_architecture_td'],
    'Dr. Lekehali': ['AI_lecture', 'AI_td'],
    'Dr. Alkama': ['Analyse_numerique_lecture', 'Analyse_numerique_td'],
    'Dr. Kaci': ['Entrepreneuriat_lecture'],
    'M. Abbas && Mme. Ladlani': ['AI_tp'],
    'Mme. Djenane': ['Securite_td'],
    'Dr. Zenadji': ['Reseaux_lecture','Reseaux_td'],
    'Mme. Khelouf': ['Securite_td'],
    'Mme. Kassa': ['Securite_td'],
    'Dr. Saba': ['Analyse_numerique_td'],
    'Dr. Djebari': ['Securite_lecture'],
    'M. Bechar': ['AI_tp']
}

GROUPS = [f'Group{num}' for num in range(1, 7)]
TD_ROOMS = [f"TD{room}" for room in range(1, 26)]
TP_ROOMS = [f"TP{room}" for room in range(1, 12)]
LECTURE_ROOMS = [f"Amphi{room}" for room in range(1, 3)]
CLASSROOMS = TD_ROOMS + TP_ROOMS + LECTURE_ROOMS
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

def generate_time_slots():
    start_time = datetime.strptime("08:30", "%H:%M").time()
    slots = []
    for i in range(5):  # 5 sessions per day
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=90)).time()
        slots.append((start_time.strftime("%H:%M"), f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"))
        start_time = (datetime.combine(datetime.today(), end_time) + timedelta(minutes=10)).time()
    return slots

TIME_SLOTS = [slot[0] for slot in generate_time_slots()]

def generate_timetable():
    slots = []
    lecture_modules = [module for module in MODULES if '_lecture' in module]
    other_modules = [module for module in MODULES if '_lecture' not in module]

    # Track the number of lectures scheduled per day
    lecture_count_per_day = {day: 0 for day in DAYS}

    # Assign lectures
    for day in DAYS:
        lecture_session = False  # Flag to track if a lecture session is being scheduled
        for i, slot in enumerate(TIME_SLOTS):
            if day == 'Tuesday' and i >= 3:
                break  # Stop generating slots after the third session on Tuesday
            if lecture_modules and lecture_count_per_day[day] < 2:
                module = lecture_modules.pop(0)
                teacher = None
                for t, modules in TEACHERS.items():
                    if module in modules:
                        teacher = t
                        break
                if teacher is None:
                    teacher = 'Substitute'
                classroom = LECTURE_ROOMS[0]  # Assuming all lectures are held in the first lecture room
                slots.append(TimetableSlot(
                    day=day,
                    start_time=slot,
                    module_name=module,
                    teacher_name=teacher,
                    group_name="; ".join(GROUPS),  # All groups
                    classroom_name=classroom
                ))
                lecture_count_per_day[day] += 1
                lecture_session = True  # Set flag for lecture session

            # If a lecture session is being scheduled, skip assigning TD or TP sessions
            if lecture_session:
                continue

            # Assign other sessions (TD, TP)
            for group in GROUPS:
                if other_modules:
                    module = other_modules.pop(0)
                    teacher = None
                    for t, modules in TEACHERS.items():
                        if module in modules:
                            teacher = t
                            break
                    if teacher is None:
                        teacher = 'Substitute'
                    classroom = CLASSROOMS.pop(0) if CLASSROOMS else 'Online'
                    slots.append(TimetableSlot(
                        day=day,
                        start_time=slot,
                        module_name=module,
                        teacher_name=teacher,
                        group_name=group,
                        classroom_name=classroom
                    ))

    return slots
