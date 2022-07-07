from http.client import responses
import profile
from django.shortcuts import redirect, render, get_object_or_404
from re import template
from unicodedata import name
from urllib import response
from click import option
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
import pdfkit
from django.urls import reverse
from io import BytesIO
from django.views import View
from xhtml2pdf import pisa
# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        skill=request.POST.get("skill","")
        about_you=request.POST.get("about_you","")
        previous_work=request.POST.get("previous_work","")
        school=request.POST.get("school","")
        
        profile=Profile(name=name,phone=phone,email=email,degree=degree,university=university,skill=skill,about_you=about_you,
                        previous_work=previous_work,school=school)
        profile.save()
        
    return render(request,'accept.html')

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=get_template("resume.html")
    html=template.render({'user_profile':user_profile})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def list(request):
    profile=Profile.objects.all()
    return render(request,"list.html",{'profile':profile})

def delete(request,id):
    userprofile=Profile.objects.get(pk=id)
    userprofile.delete()
    return redirect("list")
    