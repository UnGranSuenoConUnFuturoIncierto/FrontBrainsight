import glob
import os
import time
import cv2
import csv
from django.http import JsonResponse
from django.shortcuts import render
import nibabel as nib
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from django.template.loader import render_to_string
from . import visualization as viz

#Logica de Inicio

def cargarPacientes():
    pacientes= []
    with open("appBS/static/pacientes.csv", 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=';')
        for fila in lector_csv:
            paciente = {
                "id": fila[0],
                "nombre": fila[1],
                "edad": fila[2],
                "genero": fila[3],
                "estatura": fila[4],
                "sangre": fila[5],
                "ocupacion": fila[6],
                "foto": fila[7]
            }
            pacientes.append(paciente)
    return pacientes

def home(request):
    pacientes = cargarPacientes()
    pacientes_agrupados = [pacientes[i:i + 2] for i in range(0, len(pacientes), 2)]
    return render(request, "inicio.html", {"pacientes_agrupados": pacientes_agrupados})

#Logica de Resultado

def limpiar_imagenes_antiguas(directorio):
    for archivo in glob.glob(os.path.join(directorio, 'frame*')):
        os.remove(archivo)


def informacion(request):

    pacientes = cargarPacientes()
    frame_number = 50
    
    if request.method == 'POST':

        id_paciente = request.POST.get('id_paciente')

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
        
        id_datos = "00" + id_paciente
        flair, t1, t1ce, t2, test_mask = viz.getImageTrainData(id_datos)
        viz.getFrame(t1, frame_number, temp_image_path1)
        viz.getFrame(t2, frame_number, temp_image_path2)
        viz.getFrame(flair, frame_number, temp_image_path3)
        viz.getMask(test_mask, frame_number,temp_image_path4)

        context = {
            'frame_t1_path': temp_image_path1.split('appBS/static/')[-1],
            'frame_t2_path': temp_image_path2.split('appBS/static/')[-1],
            'frame_flair_path': temp_image_path3.split('appBS/static/')[-1],
            'frame_mask_path': temp_image_path4.split('appBS/static/')[-1],
        }

        html_content = render_to_string('actualizar.html', context)
        paciente = pacientes[int(id_paciente)-1]

        return JsonResponse({"html": html_content, "paciente": paciente})
    
    else:
        id_paciente = request.GET.get('id_paciente')
        paciente = pacientes[int(id_paciente)-1]
        id_datos = "00" + id_paciente
        viz.create3DBrainWithTumor_Train(id_datos)
        viz.modify_glb_for_transparency("appBS/static/3d/prueba.glb")
        
    
    return render(request, 'informacion.html', {"paciente": paciente})