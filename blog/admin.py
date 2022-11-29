from django.contrib import admin
from .models import Room, Amenity, Fileupload

@admin.register(Fileupload)
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
    )

@admin.action(description='asd')
def reset_prices(model_admin, request, queryset):
    print(model_admin)
    # print(request)
    # print(queryset)
    pass

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    # 관리자창 정보띄우기, 필터링은 6.4

    actions = (reset_prices,)

    list_display = (
        'name',
        'country',
        'kind',
        'owner',
        'created',
 #       'rating',
        'total_amenities',
    )
    # common 정보 눌렀을 때 보기
    readonly_fields =(
        'created',
    )
    # 검색창
    search_fields = (
        'name',
        'kind',
    )

    def total_amenities(self, room):
        return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass

# Register your models here.
