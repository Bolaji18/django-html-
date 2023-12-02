from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Infos

from .models import UploadImage
from .models import UploadImage
from .models import Users
from .models import Userinfos
from django.contrib.auth import authenticate
from .forms import NewUserForm
from .forms import ads
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def nonusers(request):
    User = Users.objects.all().values()
    User = Users.objects.all()
    link = "login/"
    login = "login here"
    return render(request, 'index1.html', {'Users': User, 'link':link,'login':login })

def laropad(request):
    return render(request, 'laporad-index.html', {})

def laropad_login(request):
  return render(request, 'laporad-about.html', {})


def about(request):

    return render(request, 'about.html', {})

def log(request):
    style = "we offer logistics and planning offers for easy and secure trading"
def rent(request):
    if request.method == "POST":
        form = ads(request.POST)
        if form.is_valid():
            price = form.cleaned_data['price']
            content = form.cleaned_data['content']
            duration = form.cleaned_data['duration']
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            image1 = form.cleaned_data['image1']
            image2 = form.cleaned_data['image2']
            image3 = form.cleaned_data['image3']
            user_info = Users(price=price, content=content, duration=duration, address=address, contact=contact, image1=image1, image2=image2, image3=image3)
            user_info.save()
            return render(request=request, template_name="laporad-about.html", context={})


    form = ads()
    return render(request=request, template_name="landingpage.html", context={"form": form})

def posted(request):
      tit = request.POST['title']
      cont = request.POST['content']
      pri = request.POST['price']
      adds = request.POST['address']
      conta = request.POST['contact']
      imagine = request.FILES['images']
      imagines = request.FILES['images1']
      imagined = request.FILES['images2']
      member = Users(duration=tit, content=cont, price=pri, address=adds, contact=conta, image1=imagine, image2=imagines, image3=imagined)
      member.save()
      return HttpResponse("success")


def new(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           messages.success(request, "Registration successful")
           return HttpResponseRedirect('login/')


       messages.error(request, "Unsuccessful registration")
   form= NewUserForm()
   life= "create account"
   return render(request=request, template_name="laporad-about.html", context={"register_form":form, 'life':life})


def user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                welcome = f"you are now logged in as {username}."
                homeplace = "rent"
                ego = "Create an ad"
                ser = Users.objects.all().values()
                ser = Users.objects.all()
                context = {
                    'Users': ser,
                    'welcome': welcome,
                    'homeplace': homeplace,
                    'ego':ego,

                }
                if request.method == "POST":
                    form = ads(request.POST)
                    if form.is_valid():
                        user = form.save
                        return HttpResponse('saved')

                form = ads()
                return render(request=request, template_name="landingpage.html", context={"form": form})

                return HttpResponse(template.render(context, request))
            else:
                 messages.error(request, "invalid username or password.")

        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    create = "newaccount/"
    used = "create new user"
    life = "login"
    return render(request, "laporad-about.html", {"register_form":form,  'create':create, 'used':used, 'life':life})

def advertisement(request, id):
    User = Users.objects.get(id=id)
    return render(request, 'adpage.html', {'Users': User})

def create_ad(request,id):
    if user is not None:
        login(request, user)
        welcome = f"you are now logged in ."
        homeplace = "rent"
        ego = "Create an ad"
        ser = Users.objects.all().values()
        ser = Users.objects.all()
        template = loader.get_template('index1.html')
        context = {
            'Users': ser,
            'welcome': welcome,
            'homeplace': homeplace,
            'ego': ego,

        }
