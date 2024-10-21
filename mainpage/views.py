from django.shortcuts import render

from .models import *


def main_banner(request):
    main_info = PersonalInfo.objects.all()
    additionalInfo = AdditionalInfo.objects.all()
    experience = Experience.objects.all()
    workexperience = WorkExperiance.objects.all()
    portfolio = Portfolio.objects.all()
    return render(
        request,
        "base.html",
        {
            "main_info": main_info,
            "additionalInfo": additionalInfo,
            "experience": experience,
            "workexperience": workexperience,
            "portfolio": portfolio,
        }
    )