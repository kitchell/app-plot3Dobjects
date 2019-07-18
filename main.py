#!/usr/bin/env python
"""
Created on Sun Jul 16 20:08:14 2017

@author: lindseykitchell
"""

from render3D import Render_3D
from renderall import Render_All
import json
from xvfbwrapper import Xvfb
import os
import glob
from matplotlib import cm
import matplotlib as mpl 

# start virtual display
vdisplay = Xvfb(width=1280, height=740)
vdisplay.start()

# read json file
with open('config.json') as config_json:
    config = json.load(config_json)

color = {'Callosum_Forceps_Major_surf':[0.04850526316,0.6792842105,0.7341421053],
             'Callosum_Forceps_Minor_surf':[0.1400526316,0.7084789474,0.6680368421],
             'Left_Arcuate_surf':[0.9595947368,0.8869315789,0.1189526316], 
             'Left_Cingulum_Cingulate_surf': [0.06577894737,0.4776315789,0.8531631579], 
             'Left_Cingulum_Hippocampus_surf':[0.03562105263,0.5946210526,0.8203210526],
             'Left_Corticospinal_surf': [0.08428421053,0.3471947368,0.8573315789],
             'Left_IFOF_surf':[0.2652894737,0.7327157895,0.5916368421],
             'Left_ILF_surf':[0.5624210526,0.7486894737,0.4528842105],
             'Left_SLF_surf':[0.7996473684,0.7343736842,0.3576473684],
             'Left_Thalamic_Radiation_surf': [0.2081,0.1663,0.5292],
             'Left_Uncinate_surf':[0.9944105263,0.7464157895,0.2389842105],
             'Right_Arcuate_surf':[0.9763,0.9831,0.0538], 
             'Right_Cingulum_Cingulate_surf': [0.07765263158,0.5299631579,0.8278947368], 
             'Right_Cingulum_Hippocampus_surf':[0.02300526316,0.6443421053,0.7882842105],
             'Right_Corticospinal_surf': [0.01574736842,0.4257052632,0.8789315789],
             'Right_IFOF_surf':[0.4175631579,0.7470789474,0.5142157895],
             'Right_ILF_surf':[0.6871684211,0.7432631579,0.4029421053],
             'Right_SLF_surf':[0.9056631579,0.7261052632,0.3104684211],
             'Right_Thalamic_Radiation_surf': [0.2052473684,0.2466526316,0.6930631579],
             'Right_Uncinate_surf':[0.9847368421,0.8141052632,0.1733684211]}

if os.path.exists(config["surfaces"] +'/color.json'):
    with open(config["surfaces"] +'/color.json') as color_json:
        color_list = json.load(color_json)
    color_json_exists = 1
    color = {}
    if os.path.exists(config["surfaces"] +'/leftfrontoThalamic_Vol.*'):
        wma = 1
    else:
        wma = 0
    print wma
    for i in range(len(color_list)):
        color[color_list[i]['name'].replace(' ', '_')]=color_list[i]['color']
elif os.path.exists(config["surfaces"] +'/Callosum_Forceps_Major_surf.*'):
    color_json_exists = 0
else:
    color_json_exists = -1


norm = mpl.colors.Normalize(vmin=1, vmax=72)

#tractseg_colors = []
#list(cm.nipy_spectral(norm(n)))[0:3]

pwd = os.getcwd()
os.mkdir(pwd + "/images")


camera_pos = [(118.81, 211.04, -355.12), (571.65, 100.27, 146.49),
              (89.77, 559.43, 169.19), (-391.38, 120.76, 97.38),
              (84.96, -196.98, 65.47), (77.83, 53.93, 537.86)]
focal_point = [(90.62, 112.50, 87.50), (91.25, 111.88, 100.62),
               (90.62, 112.50, 87.50), (91.25, 111.88, 100.62),
               (90.62, 112.50, 87.50), (90.62, 112.50, 87.50)]
view_up = [(-0.02, 0.98, 0.22), (0.10, 0.08, -0.99),
           (0.02, 0.18, -0.98), (0.01, 0.19, -0.98),
           (0.04, 0.07, -1.00), (0.00, 0.99, 0.13)]
views = ['top', 'sagittal_left', 'front', 'sagittal_right', 'back', 'bottom']


#camera_pos = [(-5.58, 84.98, -467.47), (482.32, 3.58, -6.28),
#              (-58.32, 454.83, -14.22), (-455.46, 9.14, 95.68),
#              (82.61, -195.91, 120.86) ]
#focal_point = [(-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47),
#               (-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47),
#               (90.62, 112.50, 87.50)]
#view_up = [(0.05, 0.98, -0.21), (-0.02, 0.01, -1.00),
#           (-0.01, 0.04, -1.00), (-0.20, -0.21, -0.96),
#           (0.04, -0.11, -0.99)]
#views = ['top', 'sagittal_left', 'front', 'sagittal_right', 'back']


json_file = {}
file_list = []
count = 1
#for file in glob.glob('/Users/lindseykitchell/Downloads/surfaces/' + "/*.vtk"):
  
for file in glob.glob(config["surfaces"] + "/*.vtk"):
    #print file
    fname = os.path.basename(file)[0:-9]
    if color_json_exists == 1:
        if wma:
            fname=os.path.basename(file)[0:-4]
            fname_color = os.path.basename(file)[0:-4]
        else:
            fname = os.path.basename(file)[0:-9]
            fname_color = os.path.basename(file)[0:-9]
    elif color_json_exists == 0:
        fname = os.path.basename(file)[0:-9]
        fname_color = os.path.basename(file)[0:-4]
    elif color_json_exists == -1:
        fname = os.path.basename(file)[0:-4]
        fname_color = ''     
    if fname_color in color.keys():
#for file in glob.glob('surfaces/*.vtk'):
        for d in range(len(camera_pos)):
            Render_3D(file, views[d], camera_pos[d], focal_point[d], view_up[d], color[fname_color])
            temp_dict = {}
            if wma:
                temp_dict["filename"]='images/'+fname+'_Vol_'+views[d]+'.png'
            else:
                temp_dict["filename"]='images/'+fname+'_surf_'+views[d]+'.png'
            temp_dict["name"]=fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            temp_dict["desc"]= 'This figure shows '+ fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            file_list.append(temp_dict)

    else:
#        image_color = [0.06577894737,0.4776315789,0.8531631579]
        image_color = list(cm.rainbow(norm(count)))[0:3]
        for d in range(len(camera_pos)):
            Render_3D(file, views[d], camera_pos[d], focal_point[d], view_up[d], image_color)
            temp_dict = {}
            temp_dict["filename"]='images/'+fname+'_'+views[d]+'.png'
            temp_dict["name"]=fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            temp_dict["desc"]= 'This figure shows '+ fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            file_list.append(temp_dict)
    
    count += 1
    
for d in range(len(camera_pos)):
    Render_All(config["surfaces"], views[d], camera_pos[d], focal_point[d], view_up[d], norm)
    temp_dict = {}
    temp_dict["filename"]='images/'+'all_surfaces_'+views[d]+'.png'
    temp_dict["name"]='All surfaces ' +views[d].replace('_', ' ') + ' view'
    temp_dict["desc"]= 'This figure shows all surfaces'+' '+views[d].replace('_', ' ') + ' view'
    file_list.append(temp_dict)

    
json_file['images'] = file_list
with open('images.json', 'w') as f:
    f.write(json.dumps(json_file, indent=4))

if config['remove_background']:
    import cv2
    def removebkgrd(filename):
        src = cv2.imread(filename, 1)
        tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
        b, g, r = cv2.split(src)
        rgba = [b,g,r, alpha]
        dst = cv2.merge(rgba,4)
        cv2.imwrite(filename, dst)
    for file in glob.glob(pwd+'/images/*.png'):
        removebkgrd(file)

print len(file_list)
  
vdisplay.stop()
