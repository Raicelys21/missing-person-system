from cgi import print_arguments
from django.shortcuts import render
from .forms import GalleryForm, IdentifyForm
from .models import Gallery, Identify
import os, glob
from cgi import print_arguments
import cv2
#import face_recognition


def addElement(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = GalleryForm()
    images = Gallery.objects.all()
    return render(request, 'index.html', {'images': images, 'form': form})


def compareElement(request2):
    if request2.method == "POST":
        form2 = IdentifyForm(request2.POST, request2.FILES)
        if form2.is_valid():
            form2.save()
    form2 = IdentifyForm()
    images2 = Identify.objects.all()
    return render(request2, 'compare.html', {'images2': images2, 'form2': form2})


def executeCompare(request3):
    form2 = IdentifyForm()
    images2 = Identify.objects.all()
    '''
    path_of_the_directory = 'C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/identify'
    object = os.scandir(path_of_the_directory)
    path_of_the_directory0 = 'C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/gallery'
    object0 = os.scandir(path_of_the_directory0)

    for n in object:
        if n.is_file():
            ReadImage1 = cv2.imread(n)
            ReadImage1 = cv2.cvtColor(ReadImage1, cv2.COLOR_BGR2RGB)
            ReadImage1_encoding = face_recognition.face_encodings(ReadImage1)[0] 
            for n in object0:
                if n.is_file():
                    ReadImage2 = cv2.imread(n)
                    ReadImage2 = cv2.cvtColor(ReadImage2, cv2.COLOR_BGR2RGB)
                    ReadImage2_encoding = face_recognition.face_encodings(ReadImage2)[0]

    Resultado = face_recognition.compare_faces(
        [ReadImage1_encoding], ReadImage2_encoding)
    
    cv2.imshow('img', ReadImage1)
    cv2.waitKey(0)
    cv2.imshow('img2', ReadImage2)
'''
    return  render(request3, 'compare.html', {'images2': images2, 'form2': form2})


def delete_all(request4):
    Identify.objects.all().delete()
    dir = 'C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/identify'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

    form2 = IdentifyForm()
    images2 = Identify.objects.all()
    return render(request4, 'compare.html', {'images2': images2, 'form2': form2})