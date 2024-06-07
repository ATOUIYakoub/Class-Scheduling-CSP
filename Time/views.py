from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import TimetableSlot
from .serializers import TimetableSlotSerializer
from .csp_utils import generate_timetable

class TimetableListCreate(generics.ListCreateAPIView):
    queryset = TimetableSlot.objects.all()
    serializer_class = TimetableSlotSerializer

    def get(self, request, *args, **kwargs):
        timetable = generate_timetable()
        serializer = TimetableSlotSerializer(timetable, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
