from rest_framework import serializers, viewsets

from .models import Record

class RecordSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Record

class RecordViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer
