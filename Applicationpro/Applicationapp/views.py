from django.shortcuts import render, get_list_or_404
from .forms import NewFormPerson
from .models import Person



#Create your views here.


def index(request):
    allPerson = Person.object.all()
    return render(request, 'Applicationapp/index.html'{ name_list: allPerson})

    



# add for my view #
#def name(request):
    #new_form #= NewFormPerson(request.'POST' or None)
    #if new_form_is_vaild():
        #new_form.save()