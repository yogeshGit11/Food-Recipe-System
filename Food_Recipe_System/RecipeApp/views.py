
from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from requests import request
from .models import AllRecipes
from .forms import AddRecipe,signinform,signupform
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.

class MyRecipe(View):
    def get(self,request):
        return render(request,'web/home.html')

class ShowRecipe(View):
    
        def get(self,request):
            if request.user.is_authenticated:
                if 'src' in request.GET:
                    src=request.GET['src']
                    rcplist=AllRecipes.objects.filter(recipe_title=src)
                else:
                    rcplist=AllRecipes.objects.all()
                    
                pagination=Paginator(rcplist,3)
                page_num=request.GET.get('page')
                obj=pagination.get_page(page_num)
                
                return render(request,'web/recipeList.html',{'list':obj})

            else:
                return HttpResponseRedirect('/SignIn/')

class AddRcp(View):
    
    def get(self,request):
        if request.user.is_authenticated:
            rcp=AddRecipe()
            return render(request,'web/add_recipe.html',{'rcp':rcp})

        else:
                return  HttpResponseRedirect('/SignIn/')

    def post(self,request):
        if request.user.is_authenticated:
            rcp=AddRecipe(request.POST)
            if rcp.is_valid():
                rcp.save()
                rcp=AddRecipe()
                messages.success(request,'Recipe Added Successfully!')

            return render(request,'web/add_recipe.html',{'rcp':rcp})

        else:
              return HttpResponseRedirect('/SignIn/')


def editrcp(request,id):
    if request.method=='POST':
        upid=AllRecipes.objects.get(pk=id)
        rcp=AddRecipe(request.POST,instance=upid)
        if rcp.is_valid():
            rcp.save()
            rcp=AddRecipe()
    else:
        upid=AllRecipes.objects.get(pk=id)
        rcp=AddRecipe(instance=upid)

    return render(request,'web/edit_recipe.html',{'rcp':rcp})
        

def visiteOwner(request,id):
    shid=AllRecipes.objects.get(pk=id)

    nm=AllRecipes.objects.get(pk=id)
    
    return render(request,'web/show_owner.html',{'name':nm})


class signup(View):
    def get(self,request):
        sup=signupform()
        return render(request,'web/signup.html',{'form':sup})

    def post(self,request):
        sup=signupform(request.POST)
        if sup.is_valid():
            sup.save()
            sup=signupform()
            messages.success(request,'Sign up successfully!!!')
        return render(request,'web/signup.html',{'form':sup})

class signin(View):
        def get(self,request):
            if not request.user.is_authenticated:
                sin=signinform()

                return render(request,'web/signIn.html',{'form':sin})

            else:
                return  HttpResponseRedirect('/')

            

        def post(self,request):
            if not request.user.is_authenticated:
                sin=signinform(data=request.POST,request=request)
                if sin.is_valid():
                    uname=sin.cleaned_data['username']
                    upass=sin.cleaned_data['password']

                    user=authenticate(username=uname,password=upass)

                    if user is not None:
                        login(request,user)
                        messages.success(request,'Welcome :)')
                        return HttpResponseRedirect('/')
                return render(request,'web/signIn.html',{'form':sin})

            else:
                return  HttpResponseRedirect('/')


def deleterp(request,id):
    if request.method=='POST':
        delid=AllRecipes.objects.get(pk=id)
        delid.delete()

    return HttpResponseRedirect('/ShowRecipes/')

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/SignIn/')

def aboutpage(request):
    return render(request,'web/about.html')