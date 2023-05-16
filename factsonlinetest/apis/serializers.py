# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import LangModel

# Create a model serializer
class LangSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = LangModel
		fields = ('lang_name', 'description')
