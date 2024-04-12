from django.shortcuts import render
from .models import CleanupActivity

def activity_list(request):
    activities = CleanupActivity.objects.all()
    return render(request, 'waste_management/activity_list.html', {'activities': activities})
