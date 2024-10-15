from django.contrib import admin

from .models import PersonalInfo, AdditionalInfo, Experience


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(AdditionalInfo)
class AdditionalInfo(admin.ModelAdmin):
    pass

@admin.register(Experience)
class Experience(admin.ModelAdmin):
    pass
