from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUerAdmin(UserAdmin):
    fieldsets = (
        # 유저 정보 수정
        (
            "Profile", 
            {
                "fields": ("avatar","username", "password", "name",
                "email", "is_host","gender",),
            },
        ),
        # 권한 허용
        (
            'Permissions',
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',),
                # 보기 감추기
                "classes":("collapse",),
            }
        ),
    )
    pass 