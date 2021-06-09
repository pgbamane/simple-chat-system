from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'chat_app/index.html')


@login_required
def room(request, room_name):
    print("Username: " + request.user.username)
    return render(request, 'chat_app/room.html', {
        'room_name': room_name,
        'username': request.user.username
    })
