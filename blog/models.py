from django.db import models
from common.models import CommonModel
 

# Create your models here.

class Fileupload(models.Model):
    title = models.CharField(max_length=200)
    imgfile = models.ImageField(null=True, upload_to='%Y/%m/%d/', blank=True)
    latitude = models.FloatField(max_length=200,blank=True, default=0)
    longitude = models.FloatField(max_length=200,blank=True, default=0)
    tmp = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Filereceive(models.Model):
    #title = models.CharField(max_length=200)
    tmp = models.CharField(max_length=200, blank=True)


# img loc function
class Receivedata(CommonModel):

    tmp = models.CharField(max_length=200, default='')

class Room(CommonModel):

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ('entire_place', 'Entire Place')
        PRIVATE_PLACE = ('private_place', 'Private Place')
    
    name = models.CharField(max_length=180, default='')
    country = models.CharField(max_length=50, default='한국')
    city = models.CharField(max_length=80, default='서울')
    rooms = models.PositiveBigIntegerField()
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    # model 연결을 위한 키 지정(지금은 종속관계임을 지정), related_name은 유저가 호출시 이름 지정
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='rooms',null=True)
    # many to many(amenity 연결), related_name안하면 뒤에 _set붙여야함
    amenities = models.ManyToManyField("blog.Amenity", related_name='rooms',null=True)

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        print(self.amenities.count())
        return self.amenities.count()
    
    # def rating(room):
    # #     # tmp=room.experience_set.all()
    # #     # ttmp=''
    # #     # for i in tmp:
    # #     #     ttmp+=i.name
    # #     # return ttmp
    #     return room.experience_set.all()[0].name


class Amenity(CommonModel):

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="", null=True)

    # admin관리자에서 속성이름 변경
    def __str__(self) -> str:
        return self.name

import exifread as ef



def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


def getGPS(filepath):
    '''
    returns gps data if present other wise returns empty dictionary
    '''
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        latitude = tags.get('GPS GPSLatitude')
        latitude_ref = tags.get('GPS GPSLatitudeRef')
        longitude = tags.get('GPS GPSLongitude')
        longitude_ref = tags.get('GPS GPSLongitudeRef')
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != 'N':
                lat_value = -lat_value
        else:
            return {}
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != 'E':
                lon_value = -lon_value
        else:
            return {}
        return {'latitude': lat_value, 'longitude': lon_value}
    return {}
