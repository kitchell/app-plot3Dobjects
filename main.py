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

pwd = os.getcwd()
os.mkdir(pwd + "/images")

camera_pos = [(-5.58, 84.98, 467.47), (-482.32, 3.58, -6.28),
              (-58.32, 454.83, -14.22), (455.46, 9.14, 95.68)]
focal_point = [(-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47),
               (-8.92, -16.15, 4.47), (-8.92, -16.15, 4.47)]
view_up = [(0.05, 0.98, -0.21), (-0.02, -0.01, 1.00),
           (-0.01, 0.04, 1.00), (-0.20, 0.21, 0.96)]
views = ['axial', 'sagittal_left', 'coronal', 'sagittal_right']

for file in glob.glob(config["surfaces"] + "/*.vtk"):
    print file
#for file in glob.glob('surfaces/*.vtk'):
    for d in range(len(camera_pos)):
        Render_3D(file, views[d], camera_pos[d], focal_point[d], view_up[d])
        

vdisplay.stop()
