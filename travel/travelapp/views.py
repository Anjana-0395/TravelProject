from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# -----Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj_team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj_team})







    # return HttpResponse("hello world")
# -----displaing whole html page
# def disp(request):
#     name1 = "passing"
#     return render(request,"home.html",{'obj1':name1})
# # -----multiple views
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("this is contact")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     s=x+y
#     return render(request,"result.html",{'sum':s})