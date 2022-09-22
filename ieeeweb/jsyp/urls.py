from django.contrib import admin
from django.urls import path
from jsyp import views
app_name='jsyp'
urlpatterns = [
    path('',views.home),
    path('home/',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/congresscomittee/',views.congresscom,name='congresscom'),
    path('contactus/ambassador/',views.embassidor,name='embassidor'),
    path('aboutus/ieee/',views.ieee,name='ieee'),
    path('aboutus/ieeeypafg/',views.ieeeypafg,name='ieeeypafg'),
    path('speakers/keynotespeech/',views.keynotespeech,name='keynotespeech'),
    path('contactus/congresscom/oandecommittee/',views.oandecom,name='oandecom'),
    path('regester/',views.regester,name='regester'),
    path('speakers/',views.speakers,name='speakers'),
    path('contactus/congresscom/steering/',views.steering,name='steering'),
    path('contactus/congresscom/volunteers/',views.volunteers,name='volunteers'),
    path('speakers/wrkshops/',views.wrkshops,name='wrkshops'),
    path('contactus/',views.contactus,name='contactus'),
    path('aboutus/ieeehusb/',views.ieeehusb,name='ieeehusb'),

]
