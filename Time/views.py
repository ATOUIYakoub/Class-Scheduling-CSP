from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from .models import TimetableSlot
from .serializers import TimetableSlotSerializer
from .csp_utils import generate_timetable

class TimetableListCreate(generics.ListCreateAPIView):
    queryset = TimetableSlot.objects.all()
    serializer_class = TimetableSlotSerializer

    def get(self, request, *args, **kwargs):
        # Generate the latest timetable
        timetable = generate_timetable()

        # Get the maximum ID generated in the current batch
        max_id = max(slot.id for slot in timetable)

        # Fetch the latest timetable slots based on the max ID
        latest_timetable_slots = TimetableSlot.objects.filter(
            id__gt=max_id - len(timetable)
        )

        # Filter based on query parameters if provided
        module_name = request.query_params.get('module_name', None)
        if module_name:
            latest_timetable_slots = latest_timetable_slots.filter(module_name=module_name)

        serializer = TimetableSlotSerializer(latest_timetable_slots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
