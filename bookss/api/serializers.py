from pyexpat import model

from rest_framework import serializers
from bookss.models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','description')
        model= Book