from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from app.models import Data
from datetime import datetime
import time
@csrf_exempt
def data_collect(request):
	if request.method == "GET":
		return render(request, "app/data_collect.html", {})
	else:
		try:
			height = float(request.POST.get("height", None))
			weight = float(request.POST.get("weight", None))
			bust = float(request.POST.get("bust", None))
			waist_circumference = float(request.POST.get("waist_circumference", None))
			hip_circumference = float(request.POST.get("hip_circumference", None))
			collect_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			collect_time = datetime.strptime(collect_time, "%Y-%m-%d %H:%M:%S")
			data = Data()
			data.height = height
			data.weight = weight
			data.bust = bust
			data.waist_circumference = waist_circumference
			data.hip_circumference = hip_circumference
			data.collect_time = collect_time
			data.save()
			return HttpResponse("success")
		except Exception as e:
			print(e)
			return HttpResponse("error")
# Create your views here.
