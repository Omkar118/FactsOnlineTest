# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import LangSerializer
from .models import LangModel

# create a viewset
class LangViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = LangModel.objects.all()

	# specify serializer to be used
	serializer_class = LangSerializer
