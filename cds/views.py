from django.shortcuts import render
from io import StringIO
from msilib.schema import File
from tempfile import NamedTemporaryFile
from tkinter import Image
from urllib.request import urlopen
from fer import FER
from django.shortcuts import render, HttpResponse
from django.contrib import messages
# Create your views here
from matplotlib import pyplot as plt
#=============================
from cds.models import cds_model
from django.http import JsonResponse
from time import time
#=============================
def home(request):
    return render(request,'index1.html')
from datetime import datetime
def hey():
    date = datetime.now().strftime("%H:%M:%S")
    return date
def cds(request):
    if request.method == "POST":
        image_ = request.FILES['image']

        print("image: ", image_)
        #=========================
        img = plt.imread(image_)

        count=1
        detector = FER(mtcnn=True)
        emotion, score = detector.top_emotion(img)
        text='hii'

        if (emotion == 'angry'):
            text = 'You are not so confident!'
            print(text)

        elif (emotion == 'happy'):
            text ='You are confident!'
            print(text)
        elif (emotion == 'sad'):
            text = 'You are not so confident!'
            print(text)
        elif (emotion == 'neutral'):
            if (score * 100 < 80):
                text = 'You are not so confident!'

            else:
                text = 'You are not so confident!'

            print(text)
        elif (emotion == 'surprise'):
            text = 'You are not so confident!'
            print(text)
        elif (emotion == 'fear'):
            text = 'You are not so confident!'
            print(text)
        count += 1
        #=========================
        #captions_ = text
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        print(text)
        date=hey()
        hii=cds_model(date=date, result=text, image=image_)
        print(image_)

        print("0000000000000000000000000000000000000000000000000")

        hii.save()

        if(text == 'You are not so confident!'):
            return render(request, 'notconfident.html')
        if (text == 'You are confident!'):
            return render(request, 'confident.html')
        else:
            return HttpResponse("Some Error had occured")
def raashi(request):
    text = request.POST.get('photo')
    print("text = ", text)
    return render(request, 'confident.html', {})