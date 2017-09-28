# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 20:08:14 2017

@author: lindseykitchell
"""

from render3D import Render_3D
import json
from xvfbwrapper import Xvfb
import os
import glob


# start virtual display
vdisplay = Xvfb()
vdisplay.start()

# read json file
with open('config.json') as config_json:
    config = json.load(config_json)

if os.path.exists(config["surfaces"] +'/color.json'):
    with open(config["surfaces"] +'/color.json') as color_json:
        color_list = json.load(color_json)
    
    color = {}
    for i in range(len(color_list)):
        color[color_list[i]['name']]=color_list[i]['color']
else:
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


pwd = os.getcwd()
os.mkdir(pwd + "/images")

camera_pos = [(-5.58, 84.98, -467.47), (482.32, 3.58, -6.28),
              (-58.32, 454.83, -14.22), (-455.46, 9.14, 95.68)]
focal_point = [(-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47),
               (-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47)]
view_up = [(0.05, 0.98, -0.21), (-0.02, 0.01, -1.00),
           (-0.01, 0.04, -1.00), (-0.20, -0.21, -0.96)]
views = ['axial', 'sagittal_left', 'coronal', 'sagittal_right']


json_file = {}
file_list = []
for file in glob.glob(config["surfaces"] + "/*.vtk"):
    #print file
    fname = os.path.basename(file)[0:-9]
    if fname in color.keys():
#for file in glob.glob('surfaces/*.vtk'):
        for d in range(len(camera_pos)):
            Render_3D(file, views[d], camera_pos[d], focal_point[d], view_up[d], color[fname])
            temp_dict = {}
            temp_dict["filename"]='images/'+fname+'_'+views[d]+'.png'
            temp_dict["name"]=fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            temp_dict["desc"]= 'This figure shows '+ fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            file_list.append(temp_dict)

    else:
        image_color = [0.06577894737,0.4776315789,0.8531631579]
        for d in range(len(camera_pos)):
            Render_3D(file, views[d], camera_pos[d], focal_point[d], view_up[d], image_color)
            temp_dict = {}
            temp_dict["filename"]='images/'+fname+'_'+views[d]+'.png'
            temp_dict["name"]=fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            temp_dict["desc"]= 'This figure shows '+ fname.replace('_', ' ')+' '+views[d].replace('_', ' ') + ' view'
            file_list.append(temp_dict)

json_file['images'] = file_list
with open('images.json', 'w') as f:
    f.write(json.dumps(json_file, indent=4))

print len(file_list)
  
vdisplay.stop()
