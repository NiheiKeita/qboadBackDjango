from rest_framework import viewsets, routers
from apiapp.models import Choice
from apiapp.serializers import ChoiceSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

router = routers.DefaultRouter()
router.register('choices', ChoiceViewSet)