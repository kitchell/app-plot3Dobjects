# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:38:08 2018

@author: lindseykitchell
"""

def Render_All(folder, view, camera_pos, focal_point, view_up, norm):

    # load VTK
    #from vtk import *
    
    import vtk
    from vtk.util.numpy_support import vtk_to_numpy
    from dipy.viz import window, actor
    import os
    import glob
    from matplotlib import cm
    
    #tractseg surfaces to ignore
    ignorefiles = ['CC.vtk', 'CA.vtk', 'FX_left.vtk', 'FX_right.vtk']    
    
    renderer = window.Renderer()
    renderer.clear()
#    renderer.set_camera(position=camera_pos[d],
#                            focal_point=focal_point[d],
#                            view_up=view_up[d])
    renderer.set_camera(position=camera_pos,
                            focal_point=focal_point,
                            view_up=view_up)
    
    count = 1                      
    # Add files
#    for file_name in glob.glob('/Users/lindseykitchell/Downloads/surfaces/' + "/*.vtk"):
    for file_name in glob.glob(folder + "/*.vtk"):
    
        color = list(cm.rainbow(norm(count)))[0:3]
        
        if file_name in ignorefiles:
            count += 1
        else:
            # Read the surface from file
            if file_name[-3:] == 'vtk':
                object = vtk.vtkPolyDataReader()
            if file_name[-3:] == 'ply':
                object = vtk.vtkPLYReader()
            if file_name[-3:] == 'stl':
                object = vtk.vtkSTLReader()
            object.SetFileName(file_name)
        
            objectMapper = vtk.vtkPolyDataMapper()
            objectMapper.SetInputConnection(object.GetOutputPort())
            objectMapper.ScalarVisibilityOff()
            
            objectActor=vtk.vtkActor()
            objectActor.SetMapper(objectMapper)
            #objectActor.GetProperty().SetColor(0.5,0.5,0.5) # grey
            #objectActor.GetProperty().SetColor(.24, .70, .44) #mediumseagreen
            #objectActor.GetProperty().SetColor(0.498039, 1, 0.831373) #springgreen
            objectActor.GetProperty().SetColor(color[0],color[1],color[2])
    
            renderer.add(objectActor)
            count += 1
    
    show_m = window.ShowManager(renderer, size=(800, 800))
#    show_m.initialize()
#    show_m.render()
#    show_m.start()
#    renderer.camera_info()

    fname = 'all_surfaces'
    fname = 'images/'+fname+'_'+view+'.png'
    window.snapshot(renderer, fname=fname, 
                        size=(800, 800), offscreen=True, order_transparent=False)  
    
