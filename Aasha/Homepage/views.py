from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import registerForm
from .models import Chat


def Index(request):
    context = {}
    return render(request, 'Homepage/home.html', context)


def login_User(request):


    print('login user function called')
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)

            return redirect(Index)
        else:
            error_message = "Sorry Invalid Username or Password"
            context={
                'error_message': error_message
            }
            return render(request,'Homepage/login.html',context)



    return render(request, 'Homepage/login.html',context)

def logout_view(request):
    context = {

    }
    auth.logout(request)
    return redirect('/home/login')

def register_User(request):


    form = registerForm()
    if (request.method == 'POST'):
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            login(request, user)
            return redirect('Index')
        print(type(form))
        print(form)



        return render(request,'Homepage/register.html',{'form':form})
    else:
        form = registerForm()
    return render(request, 'Homepage/register.html', {'form': form})




def chat(request):
    c = Chat.objects.all()
    return render(request, "Homepage/chathome.html", {'home': 'active', 'chat': c})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('chat-msg')
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()

        return redirect(chat)
    else:
        return HttpResponse('Request must be POST.')

def Messages(request):
    c = Chat.objects.all()
    return render(request, 'Homepage/messages.html', {'chat': c})
# Create your views here.


def get_help(request):

    context = {

    }
    return render(request, 'Homepage/get_help.html', context)

def about_depression(request):
    context = {

    }
    return render(request, 'Homepage/about_depression.html',context)


def stories(request):
    context = {}
    return render(request, 'Homepage/stories.html', context)

def about_depression(request):
    context = {}
    return render(request, 'Homepage/about_depression.html', context)
def how_to_help(request):
    context = {}
    return render(request, 'Homepage/how_to_help.html', context)
def signs_of_depression(request):
    context = {}
    return render(request, 'Homepage/learn_the_signs.html', context)
def know_depression(request):
    context = {}
    return render(request, 'Homepage/know_depression.html', context)

def contributors(request):
    context = {}
    return render(request, 'Homepage/contributors.html', context)
def videoprofile(request):
    context = {}
    return render(request,'Homepage/videoprofile.html',context)

def volunteer(request):
    context = {}
    return render(request,'Homepage/volunteer.html',context)
