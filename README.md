[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.131-blue.svg)](https://doi.org/10.25663/brainlife.app.131)

# app-plot3Dobjects
application to plot 3D objects in .vtk format in 4 views: axial, coronal, left and right sagittal

### Author
- Lindsey Kitchell (kitchell@indiana.edu)


### Funding 
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)

## Running the App 

### On Brainlife.io

You can submit this App online at [https://brainlife.io/app/596cdb1a88ae6f0021531d6a#](https://brainlife.io/app/596cdb1a88ae6f0021531d6a#) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
   "surfaces": "../surfaces/"
}
```
If you have singlarity install on your local machine:

3. Launch the App by executing `main`

```bash
./main
```

Otherwise:

3. execute main.py in python

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).


## Output

The output of this app will be a folder with images of the 3d surfaces.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.  

  - Python

