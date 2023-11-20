import glob
import os
import time
import cv2
from django.shortcuts import render, HttpResponse
import nibabel as nib
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def home(request):
    return render(request, "inicio.html")

def limpiar_imagenes_antiguas(directorio):
    for archivo in glob.glob(os.path.join(directorio, 'frame*')):
        os.remove(archivo)

def getTrainData(imageNum):
    scaler = MinMaxScaler()
    
    path = f"appBS\BraTS2020_TrainingData\MICCAI_BraTS2020_TrainingData\BraTS20_Training_{imageNum}"

    flair = nib.load(path + f"\BraTS20_Training_{imageNum}_flair.nii").get_fdata()
    flair = scaler.fit_transform(flair.reshape(-1, flair.shape[-1])).reshape(flair.shape)*255
    flair = flair.astype("uint8")

    t1 = nib.load(path + f"\BraTS20_Training_{imageNum}_t1.nii").get_fdata()
    t1 = scaler.fit_transform(t1.reshape(-1, t1.shape[-1])).reshape(t1.shape)*255
    t1 = t1.astype("uint8")     

    t1ce = nib.load(path + f"\BraTS20_Training_{imageNum}_t1ce.nii").get_fdata()
    t1ce = scaler.fit_transform(t1ce.reshape(-1, t1ce.shape[-1])).reshape(t1ce.shape)*255
    t1ce = t1ce.astype("uint8")   

    t2 = nib.load(path +f"\BraTS20_Training_{imageNum}_t2.nii").get_fdata()
    t2 = scaler.fit_transform(t2.reshape(-1, t2.shape[-1])).reshape(t2.shape)*255
    t2 = t2.astype("uint8")

    mask = nib.load(path + f"\BraTS20_Training_{imageNum}_seg.nii").get_fdata()
    mask = mask.astype(np.uint8)

    return flair, t1, t1ce, t2, mask

def getframe(image, i, path):
    cv2.imwrite(path,image[:,:,i])

def informacion(request):
    if request.method == 'POST':

        frame_number = int(request.POST.get('frame-number'))
        if frame_number > 149:
            frame_number = 1

        frames_dir = os.path.join('appBS/static/frames')

        if not os.path.isdir(frames_dir):
            os.makedirs(frames_dir)
        
        limpiar_imagenes_antiguas(frames_dir)

        timestamp = int(time.time())
        temp_image_path1 = f'appBS/static/frames/framet1_{timestamp}.png'
        temp_image_path2 = f'appBS/static/frames/framet2_{timestamp}.png'
        temp_image_path3 = f'appBS/static/frames/frameflair_{timestamp}.png'
        temp_image_path4 = f'appBS/static/frames/framemask_{timestamp}.png'
        
        flair, t1, t1ce, t2, test_mask = getTrainData("001")
        getframe(t1, frame_number, temp_image_path1)
        getframe(t2, frame_number, temp_image_path2)
        getframe(flair, frame_number, temp_image_path3)
        getframe(test_mask, frame_number, temp_image_path4)

        context = {
            'frame_t1_path': temp_image_path1.split('appBS/static/')[-1],
            'frame_t2_path': temp_image_path2.split('appBS/static/')[-1],
            'frame_flair_path': temp_image_path3.split('appBS/static/')[-1],
            'frame_mask_path': temp_image_path4.split('appBS/static/')[-1],
        }
        return render(request, 'informacion.html', context)
    
    return render(request, 'informacion.html')