from django.shortcuts import render
from myuser.models import myuser
from django.http import HttpResponseRedirect


# Create your views here.
def listuser(request):
    ues=myuser.objects.all()
    context={}
    context['users']=ues
    return render(request,'lst.html',context)
def Update(request,id):
    if(request.session.get('username') is not None):

        context = {}
        if (request.method == 'GET'):
            context['users']=myuser.objects.get(id=id)
            return render(request, 'update.html', context)
        else:
            myuser.objects.filter(id=id).update(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            return HttpResponseRedirect('/User/')
    else:
        return HttpResponseRedirect('/login')

def Delete(request,id):
    if (request.session.get('username') is not None):
        userdel=myuser.objects.filter(id=id).delete()
        return HttpResponseRedirect('/User/')
    else:
        return HttpResponseRedirect('/login')