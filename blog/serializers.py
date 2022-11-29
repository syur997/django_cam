from .models import Room, Amenity, Receivedata
from rest_framework import serializers

class tmpserial(serializers.ModelSerializer):
    class Meta:
        model = Receivedata
        fields = ("__all__")


class testSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        # 선택적으로 보여주거나 exclude로 보여줄 항목 제외 가능
        fields = ("__all__")

class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity

        fields = ('name', 'country', 'rooms')

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room

        fields='__all__'