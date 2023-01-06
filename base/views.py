from django.shortcuts import render


rooms = [
    { 'id':1,'name':'Learn C'},
    { 'id':2,'name':'Learn Pyhon' },
    { 'id':3,'name':'Learn Java' }
]

# Create your views here.
def home(request):
    context={'rooms':rooms }
    return render(request,'base/home.html',context)

def room(request,id):
    room=None
    for i in rooms:
      if i['id'] == int(id):
        room = i
    context={'room':room }
    return render(request,'base/room.html',context)