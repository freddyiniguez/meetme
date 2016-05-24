from django.shortcuts import render

def meeting_list(request):
	return render(request, 'meetmeapp/meeting_list.html', {})