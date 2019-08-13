from roman_to_arabic.models import Pairs
from rest_framework import viewsets, permissions
from .serializers import PairSerializer

#Pairs Viewset


class PairViewSet(viewsets.ModelViewSet):
    queryset = Pairs.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = PairSerializer

    '''def get_queryset(self):
        return self.request.user.roman_to_arabic.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)'''
