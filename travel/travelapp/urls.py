from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # ----path to the function displaying html pages
    #  path('',views.disp,name='disp'),
    #  path('about/',views.about,name='about'),
    #  path('contact/',views.contact,name='contact'),
    #  path('add/',views.addition,name='addition')

]
