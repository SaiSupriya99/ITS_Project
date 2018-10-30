from django.shortcuts import render
from django.db import connection,transaction
from django.http import HttpResponse
from .models import schedule_history
def home(request):
 cursor=connection.cursor()
 #cursor.execute('select * from a13_schedule_history')
 #row=cursor.fetchall()
 
 #data=a13_schedule_history.objects.all()
 #current_date=data.present_date
 #context={'present':current_date}
 return render(request,'a13/home.html')
 #return render(request,'a13/detail.html',context)
def data(request,token_id):
	payload={'token':token_id,'secret':"3dfb05286cdf7816b11160b70242f2c27546781ea74ade858ddebdacf92c5dd78bd4850d2740b9e8d3c36868ad110a73dc63e06406246f47edc0af18152bb49b"}
	url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
	response=requests.post(url,data=payload)
	data=response.json()
	print(data)
	data=data['student']
	print(data)
	return render(request,'a13/index.html')	
def home(request):
 return render(request,'a13/home.html')
def login1(request):
 return render(request,'a13/login1.html')
def login2(request):
 return render(request,'a13/login2.html')
def logins(request):
 return render(request,'a13/logins.html')
def Events(request):
 return render(request,'a13/Events.html')
def TimetableG(request):
 return render(request,'a13/TimetableG.html')
def RescheduleC(request):
 return render(request,'a13/RescheduleC.html')
def Viewfm(request):
 return render(request,'a13/Viewfm.html')
def TA_a(request):
 return render(request,'a13/TA_a.html')
def settings(request):
 return render(request,'a13/settings.html')
def posts(request):
 return render(request,'a13/posts.html')
def profile(request):
 return render(request,'a13/profile.html')
def index(request):
 return render(request,'a13/index.html')
def index1(request):
 return render(request,'a13/index1.html')
def a(request):
 return render(request,'a13/a.html')
def users(request):
 return render(request,'a13/users.html')
def scheduleE(request):
 return render(request,'a13/scheduleE.html')
def schedulefm(request):
 return render(request,'a13/schedulefm.html')
def secheduled(request):
 return render(request,'a13/secheduled.html')







