from django.shortcuts import render, render_to_response
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse, HttpResponse
from django.template import loader
from .models import router
from .forms import routerForm
from django.db.models import Q

# Create your views here.
def index(request):  
    routerlist = router.objects.values('id','sapid','hostname','loopback','macaddress')    
    context = {
        'routerls':routerlist
        }
    template = loader.get_template('devices/index.html')
    return HttpResponse(template.render(context,request))  

def add_router(request):
    err=""
    form=routerForm()
    context={'form': form, 'formaction':'addrouter'}
    if request.method == 'POST':
        form = routerForm(request.POST) 
        if form.is_valid():
            rcnt = router.objects.filter(Q(loopback = request.POST.get('loopback')) or Q(sapid = request.POST.get('hostname'))).count() 
            if rcnt < 1:
                form.save()
                return HttpResponseRedirect('index')
            else:
                context = {
                'err':"Unable to add router. Already exist!",
                'form': form,
                'formaction':'addrouter'
            }
        else:
            context = {
                'err':"Unable to add data!",
                'form': form, 
                'formaction':'addrouter'
            }
            
            
    template = loader.get_template('devices/form.html')   
    return HttpResponse(template.render(context,request))

def edit_router(request,id=None):
    err=""
    if id:
        rs = router.objects.get(pk=id)        
    if request.method == 'POST':
        form = routerForm(request.POST, instance=rs)       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/devices/index')            
        else:
            context = {
                'err':"Unable to update data!",
                'form': form                
            }
    else:
        form = routerForm(instance=rs)
        context = {
            'err':err,
            'form': form           
        }
    template = loader.get_template('devices/editform.html')    
    return HttpResponse(template.render(context,request))

def delete_router(request, id):
    if id:
        router.objects.filter(id=id).delete() 
    routerlist = router.objects.values('id','sapid','hostname','loopback','macaddress')       
    context = {
        'routerls':routerlist
        }
    template = loader.get_template('devices/delete.html')      
    return HttpResponse(template.render(context,request))  