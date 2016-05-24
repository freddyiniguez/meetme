from django.shortcuts import render
from django.utils import timezone
from .models import Meeting

def meeting_list(request):
	meetings = Meeting.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
	return render(request, 'meetmeapp/meeting_list.html', {'meetings':meetings})