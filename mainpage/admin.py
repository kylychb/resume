from django.contrib import admin

from .models import PersonalInfo, AdditionalInfo


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalInfo)
class AdditionalInfo(admin.ModelAdmin):
    pass
