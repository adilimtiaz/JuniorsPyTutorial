from JuniorsPy.models.leads import Lead
from JuniorsPy.serializers.leadSerializer import LeadSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer