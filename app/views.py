from cgi import print_arguments
from django.shortcuts import render
from .forms import GalleryForm, IdentifyForm
from .models import Gallery, Identify
import os, glob
from cgi import print_arguments
import cv2
import face_recognition


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


KNOWN_IMAGES_FOLDER_PATH = "C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/gallery"
KNOWN_IMAGES_FOLDER_PATH2 = "C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/identify"


def executeCompare()-> tuple[str, str]:
    image_files = os.listdir(KNOWN_IMAGES_FOLDER_PATH)
    images_path: list[str] = []

    image_files2 = os.listdir(KNOWN_IMAGES_FOLDER_PATH2)
    images_path2: list[str] = []

    for file in image_files:
        images_path.append(f"{KNOWN_IMAGES_FOLDER_PATH}/{file}")

    for file in image_files2:
        images_path2.append(f"{KNOWN_IMAGES_FOLDER_PATH2}/{file}")

    print(images_path)
    print(images_path2)
    
    ReadImage1 = cv2.imread(images_path[0])
    ReadImage1 = cv2.cvtColor(ReadImage1, cv2.COLOR_BGR2RGB)
    ReadImage1_encoding = face_recognition.face_encodings(ReadImage1)[0]

    ReadImage2 = cv2.imread(images_path2[0])
    ReadImage2 = cv2.cvtColor(ReadImage2, cv2.COLOR_BGR2RGB)
    ReadImage2_encoding = face_recognition.face_encodings(ReadImage2)[0]

    Resultado = face_recognition.compare_faces(
        [ReadImage1_encoding], ReadImage2_encoding)
    print("Resultado: ", Resultado)

    cv2.imshow('img', ReadImage1)
    cv2.waitKey(0)
    cv2.imshow('img2', ReadImage2)
    
    form2 = IdentifyForm()
    images2 = Identify.objects.all()
    return Resultado, render('compare.html', {'images2': images2, 'form2': form2})


def delete_all(request4):
    Identify.objects.all().delete()
    dir = 'C:/Users/Raicelys Suero/Documents/CST-10/Prog. Web Avanz/Missing Person System/missingperson/media/identify'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)

    form2 = IdentifyForm()
    images2 = Identify.objects.all()
    return render(request4, 'compare.html', {'images2': images2, 'form2': form2})