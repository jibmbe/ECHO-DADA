from django.shortcuts import render
from .models import Woman

def woman_list(request):
    women = Woman.objects.all()
    return render(request, 'women_empowerment/woman_list.html', {'women': women})
