from django.shortcuts import render
import requests
from .models import *
import requests
import numpy as np
import urllib.request
import cv2
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import random
media_path='D:/Projects_2021/SmartParking/SmartParkingSystem/media/parking_images/'
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image
# Create your views here.
def home(request):
    Data = parking.objects.all().order_by('-date')[:10]
    context={'Data':Data}
    return render(request,'parking.html',context)
def saveEntry(url,cam_type):
        myfile = url_to_image(url)
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               '1','2','3','4','5','6','7','8','9','0']
        name=''
        for i in range(0,5):
                num=random.randrange(0,len(alphabets))
                name=name+alphabets[num]
        cv2.imwrite(media_path+name+'.jpg',myfile)
        cv2.waitKey(0)
        DB=parking()
        DB.cam_name=cam_type
        DB.image='parking_images/'+name+'.jpg'
        DB.save()
def carEntered(request):
        print("Car Entered")
        saveEntry('http://192.168.4.128/capture?',"ENTRY")
        response = requests.get("http://192.168.4.1/entry")
        return HttpResponse('_OK')
def carExit(request):
        print("Car Exit")
        saveEntry('http://192.168.4.127/capture?',"EXIT")
        response = requests.get("http://192.168.4.1/exit")
        return HttpResponse('_OK')
