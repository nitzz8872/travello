from django.shortcuts import render
from .models import Destination

# Create your views here.
def xyz(request):
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="City that never sleeps"
    dest1.price=759
    dest1.img='destination_1.jpg'
    dest2=Destination()
    dest2.name="Hyderabaad"
    dest2.desc='First Biryani THen Sherwani'
    dest2.price=800
    dest2.img='destination_2.jpg'
    dest3=Destination()
    dest3.name="Ludhiana"
    dest3.desc="The Manchester of india"
    dest3.price=700
    dest3.img='destination_3.jpg'
    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})
