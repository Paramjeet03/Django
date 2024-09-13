from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hey every one !!!! ")

def jai_baba_ki(request):
    return HttpResponse("<h1> K gyan mittar  </h1> ")

def html(request):
    peoples=[{"Name":"paramjeet","Age":20},
             {"Name":"tenu","Age":25},
             {"Name":"sonu","Age":60},
             {"Name":"Monu","Age":30},
             {"Name":"Rahul","Age":50},]
    return render(request,"text_formatting8.html",context={"peoples":peoples})

def html_1(request):
    return render(request,"favicon.html")

def html_2(request):
    return render(request,"form.html")

def html_3(request):
    return render(request,"Header_footer.html")

def html_4(request):
    return render(request,"HYPER_LINKS_2.html")