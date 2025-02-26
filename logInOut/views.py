from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate, login, logout 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib .auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('generative_agriculture')
        else:
            messages.success(request, 'Invalid credentials!!! Please Try Again')
            return redirect('login')
    else:
      return render(request, 'authenticate/login.html',{})
def logout_user(request):
    logout(request)
    messages.success(request, 'You are Logged Out')
    return redirect('home')

def register_user(request):
    messages.success(request, 'You are Logged Out')
    return redirect('home')

# def register_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration Successful!!!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Registration Failed!!!')
#             return redirect('register')
#     else:
#         form = UserCreationForm()
#         return render(request, 'authenticate/register.html', {'form': form})

def register_user(request):
    form = None
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            messages.success(request, 'Registration Successful!!!')
            return redirect('login')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()  # An unbound form
    return render(request,'authenticate/register.html',{'form':form})
