from django.shortcuts import render,redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     { 'id':1,'name':'Learn C'},
#     { 'id':2,'name':'Learn Pyhon' },
#     { 'id':3,'name':'Learn Java' }
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context={'rooms':rooms }
    return render(request,'base/home.html',context)

def room(request,id):
    room = Room.objects.get(id=id)
    context={'room':room }
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm()
    context={ 'form': form }
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
            
    return render(request,'base/room_form.html',context)

def updateRoom(request,id):
    
   room = Room.objects.get(id=id)
   form = RoomForm(instance=room)
   context={ 'form' : form }
   if request.method == "POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return  redirect('home')
               
   return render(request,'base/room_form.html',context)

def deleteRoom(request,id):
    
   room = Room.objects.get(id=id)
   if request.method == "POST":
        room.delete()
        return  redirect('home')
                           
   return render(request,'base/delete.html',{ 'obj' :room})
