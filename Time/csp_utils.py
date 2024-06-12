from datetime import datetime, timedelta
from collections import defaultdict
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
    'Dr. Issadi': ['Recherche_operationnelle_lecture', 'Recherche_operationnelle_td'],
    'Dr. Zedek': ['Methodes_formelles_lecture', 'Methodes_formelles_td'],
    'Mr. Sahli': ['Reseaux_td'],
    'Mme. Hamma': ['AI_tp'],
    'Dr. Djenadi': ['Distributed_architecture_lecture', 'Distributed_architecture_td'],
    'Dr. Lekehali': ['AI_lecture', 'AI_td'],
    'Dr. Alkama': ['Analyse_numerique_lecture', 'Analyse_numerique_td'],
    'Dr. Kaci': ['Entrepreneuriat_lecture'],
    'M. Abbas && Mme. Ladlani': ['AI_tp'],
    'Mme. Djenane': ['Securite_td'],
    'Dr. Zenadji': ['Reseaux_lecture', 'Reseaux_td'],
    'Mme. Khelouf': ['Securite_td'],
    'Mme. Kassa': ['Securite_td'],
    'Dr. Saba': ['Analyse_numerique_td'],
    'Dr. Djebari': ['Securite_lecture'],
    'M. Bechar': ['AI_tp']
}

GROUPS = [f'Group{num}' for num in range(1, 7)]
TD_ROOMS = [f"TD{room}" for room in range(1, 26)]
TP_ROOMS = [f"TP{room}" for room in range(1, 12)]
LECTURE_ROOMS = [f"Amphi{room}" for room in range(7, 8)]
CLASSROOMS = TD_ROOMS + TP_ROOMS + LECTURE_ROOMS
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']

def generate_time_slots():
    start_time = datetime.strptime("08:30", "%H:%M").time()
    slots = []
    for i in range(5):  # 5 sessions per day
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=90)).time()
        slots.append((start_time.strftime("%H:%M"), f"{start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}"))
        start_time = (datetime.combine(datetime.today(), end_time) + timedelta(minutes=10)).time()
    return slots

TIME_SLOTS = [slot[0] for slot in generate_time_slots()]

def split_groups_among_teachers(groups, teachers):
    groups_per_teacher = defaultdict(list)
    num_groups = len(groups)
    num_teachers = len(teachers)
    for i, group in enumerate(groups):
        groups_per_teacher[teachers[i % num_teachers]].append(group)
    return groups_per_teacher

def generate_timetable(constraints=None):
    # Delete all existing timetable slots
    TimetableSlot.objects.all().delete()

    slots = []
    all_modules = MODULES.copy()
    all_teachers = TEACHERS.copy()

    # Track the sessions assigned to each group and teacher
    sessions_assigned_per_group = {group: [] for group in GROUPS}
    sessions_assigned_per_teacher = {teacher: [] for teacher in TEACHERS.keys()}
    lectures_per_day_per_group = {group: {day: 0 for day in DAYS} for group in GROUPS}
    lectures_per_day_per_teacher = {teacher: {day: 0 for day in DAYS} for teacher in TEACHERS.keys()}

    # Track classroom usage
    classroom_usage = {day: {slot: [] for slot in TIME_SLOTS} for day in DAYS}

    # Process constraints
    if constraints:
        teacher_availability = constraints.get('teacher_availability', {})
    else:
        teacher_availability = {}

    def is_teacher_available(teacher, day, slot_index):
        if teacher in teacher_availability:
            unavailable_slots = teacher_availability[teacher].get(day, [])
            if slot_index in unavailable_slots:
                return False
        return True

    # Assign lectures first
    for module in all_modules.copy():
        if '_lecture' in module:
            teacher = next((t for t, modules in TEACHERS.items() if module in modules), None)
            if teacher:
                for day in DAYS:
                    for slot_index, slot in enumerate(TIME_SLOTS):
                        if day == 'Tuesday' and slot_index >= 3:
                            break  # Stop generating slots after the third session on Tuesday
                        for classroom in LECTURE_ROOMS:
                            if classroom not in classroom_usage[day][slot]:
                                if not any(s[0] == day and s[1] == slot_index for s in sessions_assigned_per_teacher[teacher]) and \
                                        all(lectures_per_day_per_group[group][day] < 2 for group in GROUPS) and \
                                        lectures_per_day_per_teacher[teacher][day] < 2:
                                    slots.append(TimetableSlot.objects.create(
                                        day=day,
                                        start_time=slot,
                                        module_name=module,
                                        teacher_name=teacher,
                                        group_name="; ".join(GROUPS),  # All groups
                                        classroom_name=classroom
                                    ))
                                    for group in GROUPS:
                                        sessions_assigned_per_group[group].append((day, slot_index))
                                        lectures_per_day_per_group[group][day] += 1
                                    sessions_assigned_per_teacher[teacher].append((day, slot_index))
                                    lectures_per_day_per_teacher[teacher][day] += 1
                                    classroom_usage[day][slot].append(classroom)
                                    all_modules.remove(module)
                                    break
                        if module not in all_modules:
                            break
                    if module not in all_modules:
                        break

    # Assign TD and TP sessions
    for module in [m for m in MODULES if '_lecture' not in m]:
        teachers = [t for t, modules in TEACHERS.items() if module in modules]
        groups_per_teacher = split_groups_among_teachers(GROUPS, teachers)
        for teacher, groups in groups_per_teacher.items():
            for group in groups:
                assigned = False
                for day in DAYS:
                    for slot_index, slot in enumerate(TIME_SLOTS):
                        if day == 'Tuesday' and slot_index >= 3:
                            break  # Stop generating slots after the third session on Tuesday
                        if is_teacher_available(teacher, day, slot_index):
                            classroom_list = TD_ROOMS if module.endswith('_td') else TP_ROOMS
                            for classroom in classroom_list:
                                if classroom not in classroom_usage[day][slot]:
                                    if not any(s[0] == day and s[1] == slot_index for s in sessions_assigned_per_group[group]) and \
                                            not any(s[0] == day and s[1] == slot_index for s in sessions_assigned_per_teacher[teacher]):
                                        slots.append(TimetableSlot.objects.create(
                                            day=day,
                                            start_time=slot,
                                            module_name=module,
                                            teacher_name=teacher,
                                            group_name=group,
                                            classroom_name=classroom
                                        ))
                                        sessions_assigned_per_group[group].append((day, slot_index))
                                        sessions_assigned_per_teacher[teacher].append((day, slot_index))
                                        classroom_usage[day][slot].append(classroom)
                                        assigned = True
                                        break
                            if assigned:
                                break
                    if assigned:
                        break

    return slots
