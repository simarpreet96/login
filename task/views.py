from django.shortcuts import render,redirect, get_object_or_404,get_list_or_404
from .models import User
from .forms import loginForm, SignUpForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


def post_list(request):
    posts = User.objects.filter()
    return render(request,'registration/signup.html',{'posts': posts})

def post_del(requet, pk):
    post = get_object_or_404(User, pk=pk)
    post.delete()
    return redirect('post_list')

def post_edit(request, pk):
    post = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = SignUpForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = SignUpForm(instance=post)
    return render(request, 'task/post_edit.html', {'form': form})

def login(request):
    if request.method =='POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get('username')
            raw_password = form.cleaned_date.get('password')
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = loginForm()
    return render(request, 'registration/login.html', {'form':form})


def signup(request):
    posts = User.objects.filter()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form,'posts': posts})

def active(request,obj=None,parent_obj=None):
    posts = User.objects.get(is_active)
    obj=obj.User
    if obj:
        if obj.is_active==True:
            posts.is_active = True
            posts.save()
            return redirect('inactive')
        elif obj.is_active==False:
            posts.is_active = False
            posts.save()
            return redirect('isactive')
    return render(request,"registration/signup.html", {'posts':posts})

def inactive(request,obj=None,parent_obj=None):
    posts = User.objects.get(is_active)
    posts.is_active = False
    return render(request,"registration/signup.html", {'posts':posts})

def isactive(request,obj=None,parent_obj=None):
    posts = User.objects.get(is_active)
    posts.is_active = True
    return render(request,"registration/signup.html", {'posts':posts})




#def active(request):
#    userbig = User.objects.get()
#    if userbig.user.is_staff = is_staff:
#        userbig.save()
#    else:
#        userbig = User.objects.get(is_active=False)
#   return render(request, 'registration/signup.html', {'userbig':userbig})


#def active(request):
#    posts = User.objects.get(is_staff,is_active)
#    if request.method == 'POST': #* permission.is_valid():
#        posts.is_superuser = False
#        posts.is_staff = True
#        posts.save() 
#    else:
#        posts.is_active = True
#        posts.save()
#    return render(request,"registration/signup.html", {'posts':posts,})


#def active(request, obj=None):
#    actions= User.objects.get(is_active)
#    obj=obj.User
#    if obj:
#        if obj.is_active==True:
#            actions.append('isactive')
#        elif obj.is_active==False:
#            actions.append('inactive')
#        return actions

#    def isactive(request, obj, parent_obj=None):
#        obj.is_active=False
#        obj.save()
#        messages.info(request,_("User is active."))
#    isactive.short_description=_("active")

#    def inactive(request, obj, parent_obj=None):
#        obj.is_active=True
#        obj.save()
#        messages.info(request,_("User is not active."))
#    inactive.short_description=_("NotActive")


#def active(request,obj=None,parent_obj=None):
#    user = authenticate(username,password)
#    if user is not None:
#        if user.is_active:   
#            user.is_active = False
#        else:
#            user.is_active = True
#    else:
#       return render(request, 'registration/signup.html', {'userbig':userbig})

