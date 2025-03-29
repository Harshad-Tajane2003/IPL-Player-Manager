from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages  # For flash messages, if needed
from iplapp.models import Player

# Create your views here.
def home_view(request):
    return render(request, "iplapp/home.html")


# Login view

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("un")
        password = request.POST.get("pwd")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('iplapp:home')  # Redirect to the home page
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('iplapp:login')  # Redirect back to the login page
    
    return render(request, "iplapp/login.html")


   


def signup_view(request):
    if request.method == "POST":  # Ensure it's a POST request
        # Get data from the form
        un = request.POST.get("un")
        pwd = request.POST.get("pwd")
        mail = request.POST.get("mail")
        
          # Check if the username already exists
        if User.objects.filter(username=un).exists():
            messages.error(request, "User already exists. Please choose another username.")
            return redirect("iplapp:signup")  # Redirect to the signup page if user exists
    
        # Check if any field is empty, if so, add a message
        if not un or not pwd or not mail:
            messages.error(request, "Please fill in all fields")
            return redirect("iplapp:signup")
        
        # Create user
        try:
            user = User.objects.create_user(username=un, email=mail, password=pwd)
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("iplapp:login")  # Redirect to login page after successful registration
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return redirect("iplapp:signup")
    
    return render(request, "iplapp/signup.html")
















# from django.shortcuts import redirect, render
# from django.contrib.auth.models import User
# from iplapp.models import Player


# # Create your views here.
# def home_view(request):
#     return render(request,"iplapp/home.html")


# def login_view(request):
#     return render(request,"iplapp/login.html")

# def signup_view(request):
#     if request.method=="post":
#         print(request.POST)
#         un=request.POST.get("un")
#         pwd=request.POST.get("pwd")
#         mail=request.POST.get("mail")
#         print(un,pwd,mail)
        
#         User.objects.create_user(username=un, email=mail, password=pwd)
#         return redirect("iplapp/login/")
    
#     return render(request,"iplapp/signup.html")
    
    # if request.method=="post":
    #     un=request.POST.get("un")
    #     pwd=request.POST.get("pwd")
    #     # mail=request.POST.get("mail")
    #     obj=User.objects.get(username=un)
    #     if(obj.password == pwd and obj.username == pwd):
    #         login(request)
    #         return redirect("/iplapp/home/")
    #     else:
    #         return render


def create_view(request):
    
    if request.method=="POST":
        print(request.POST)
        print("HELLO")
        j=request.POST.get("jno")
        n=request.POST.get("pname")
        r=request.POST.get("runs")
        w=request.POST.get("wickets")
        t=request.POST.get("tname")
        obj=Player(jno=j,pname=n,runs=r,wickets=w,tname=t)
        obj.save()
        return redirect("/iplapp/display/")
    
    return render(request,"iplapp/create.html")

def display_view(request):
    data=Player.objects.all()
    context={"data":data}
    return render(request,"iplapp/display.html",context)


def update_view(request,n):
    
    obj = Player.objects.get(jno=n)
    context={"p":obj}
    
    if request.method =="POST":
        print(request.POST)
 
        # u_j=request.POST.get("jno")
        u_n=request.POST.get("pname")
        u_r=request.POST.get("runs")
        u_w=request.POST.get("wickets")
        u_t=request.POST.get("tname")
        
        # obj.jno=u_j
        obj.pname=u_n
        obj.runs=u_r
        obj.wickets=u_w
        obj.tname=u_t
        obj.save()
        return redirect("/iplapp/display/")
    
    return render(request,"iplapp/update.html",context)


def delete_view(request,n):
    obj = Player.objects.get(jno=n)
    obj.delete()
    return redirect ("/iplapp/display/")