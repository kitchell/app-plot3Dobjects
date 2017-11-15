
FROM neurodebian:nd16.04

MAINTAINER Lindsey Kitchell <kitchell@indiana.edu>

RUN apt update && \
    apt install -y git python-vtk python-numpy python-scipy python-pip x11vnc xvfb
#RUN pip install h5py dicom six Cython scipy tables opencv-python 
RUN pip install xvfbwrapper dipy nibabel opencv-python numpy
#RUN git clone https://github.com/nipy/nibabel.git /nibabel
#RUN cd /nibabel && python setup.py build_ext --inplace
#RUN git clone https://github.com/nipy/dipy.git /dipy
#RUN cd /dipy && PYTHONPATH=/nibabel python setup.py build_ext --inplace
#RUN git clone https://github.com/cgoldberg/xvfbwrapper.git /xvfbwrapper
#RUN cd /xvfbwrapper && PYTHONPATH=/xvfbwrapper python setup.py build_ext --inplace

COPY main.py /main.py
COPY render3D.py /render3D.py 

#ENV PYTHONPATH /dipy:$PYTHONPATH
#ENV PYTHONPATH /nibabl:$PYTHONPATH
#ENV PYTHONPATH /xvfbwrapper:$PYTHONPATH
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages

RUN mkdir /output && ldconfig

WORKDIR /output
ENTRYPOINT ["/main.py"]
