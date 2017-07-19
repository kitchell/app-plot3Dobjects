# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 18:45:22 2017

@author: lindseykitchell
"""


def Render_3D(file_name, view, camera_pos, focal_point, view_up):

    # load VTK
    #from vtk import *
    
    import vtk
    from vtk.util.numpy_support import vtk_to_numpy
    from dipy.viz import window, actor
    import os
    
    # Read the surface from file
    object = vtk.vtkPolyDataReader()
    object.SetFileName(file_name)
    
    objectMapper = vtk.vtkPolyDataMapper()
    objectMapper.SetInputConnection(object.GetOutputPort())
    objectMapper.ScalarVisibilityOff()
    
    objectActor=vtk.vtkActor()
    objectActor.SetMapper(objectMapper)
    #objectActor.GetProperty().SetColor(0.5,0.5,0.5)
    objectActor.GetProperty().SetColor(.24, .70, .44)
    # Attach to a renderer
#    ren = vtk.vtkRenderer()
#    ren.AddActor(objectActor)
#    ren.SetBackground(0.1, 0.1, 0.1)
    
    # Attach to a window
#    renWin = vtk.vtkRenderWindow()
#    renWin.AddRenderer(ren)
#    #renWin.SetWindowName("surface")
#    renWin.SetSize(500,500)
    
    # Attach to an interactor
#    iren = vtk.vtkRenderWindowInteractor()
#    iren.SetRenderWindow(renWin)
#    style = vtk.vtkInteractorStyleSwitch()
#    style.SetCurrentStyleToTrackballCamera()
#    iren.SetInteractorStyle(style)
#    iren.Initialize()
#    iren.Start()
#    
   
    renderer = window.Renderer()
    renderer.clear()
    renderer.set_camera(position=camera_pos,
                            focal_point=focal_point,
                            view_up=view_up)
    renderer.add(objectActor)
    show_m = window.ShowManager(renderer, size=(800, 800))
#    show_m.initialize()
#    show_m.render()
#    show_m.start()

    fname = os.path.basename(file_name)
    fname = 'images/'+fname[0:-4]+'_'+view+'.png'
    window.snapshot(renderer, fname=fname, 
                        size=(800, 800), offscreen=True, order_transparent=False)  
    
