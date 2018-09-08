from django.shortcuts import render
# Create your views here.
 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.models import Check
from accounts.models import Book
from django.contrib.auth.models import User

# from .models import Detail
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class details(request):
#     cost = Check.objects.get(Source=Source)
def CheckPage(request):
    print(request.method)
    if request.method == "GET":
        return render(request,'check.html')
    
    if request.method == "POST":
        source = request.POST["Source"]
        destination = request.POST["Destination"]
        print('Source: :'+source+': Dest: :'+destination+':')
        # print(str(len(Check.objects.all())))
        # print(Check.objects.all())
        check = Check.objects.filter(source=source, destination=destination)
        print(' length '+str(len(check)))
        costt = check[0].cost
        try:
            costt = check.cost
        except:
            pass
        print('Cost: '+str(costt))
        return render(request, 'check.html', {'cost': costt})
        

def Home(request):
    book_count = -1
    if checkLogin(request):
        book_count = Book.objects.filter(user=User.objects.filter(id=request.user.id)[0]).count()
    return render(request,'home.html', {'book_count':book_count})    


def BookPage(request):
    
    if request.method == "GET":
        return render(request,'book.html')

    if request.method == "POST":
        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id)
            if user is not None:
                book1 = Book()
                print('Booking started')
                book1.user = user[0]
                book1.name = request.POST["Name"]
                book1.source = request.POST["Source"]    
                book1.destination = request.POST["Destination"]
                book1.date = request.POST["Date"]
                book1.tclass = request.POST["TClass"]
                book1.flight = request.POST["Flight"]
                book1.save()
            else:
                print('User not found')
        else:
            print('User not authenticated(Might be user not logged in)')

        # print(' length '+str(len(book1)))
        return render(request,'book.html')
    # if request.method == "POST":
    #     source = request.POST["Source"]
    #     destination = request.POST["Destination"]

def checkLogin(request):
    if request.user.is_authenticated:
        return True
    else:
        return False


def Detail(request):
    booking = []
    print(checkLogin(request))
    if checkLogin(request):

        user = User.objects.filter(id=request.user.id)
        print(user)
        if user is not None:
            booking = Book.objects.filter(user=user[0])
            print(booking)

    return render(request,'details.html', {'booking': booking})  

# class Entry(CreateView):
#     model = Book
#     fields=['name','source','destination','date','coach']

# class DetailView(generic.ListView):
#     obj_name = 'booking_list'
#     template_name = 'accounts/index.html'

#     def get_queryset(self):
#         return Book.objects.all()