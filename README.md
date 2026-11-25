<h1 align="center">Plot 3D Surfaces</h1>

<p align="center">
  Renders 3D surface meshes (.vtk), such as tract surfaces, as PNG images from six camera views with VTK; currently cannot run on any brainlife resource.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.131"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.131-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Renders 3D surface meshes (.vtk), such as tract surfaces, as PNG images from six camera views with VTK; currently cannot run on any brainlife resource.**

Visualisation utility: loads every .vtk surface in the input directory, colours known tract surfaces (or uses the input's color.json), and renders top, bottom, front, back and left/right sagittal views under a virtual display, writing PNGs and images.json. As the registry notes, main activates a local 'dipyenv' conda environment instead of a container, so the App must be updated to run via Singularity before it can be used.

| | |
|---|---|
| **Inputs** | `neuro/3Dsurfaces` |
| **Outputs** | `generic/images` |
| **Resources** | 8 CPUs · 0.33 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.131](https://doi.org/10.25663/brainlife.app.131) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `surfaces` | `neuro/3Dsurfaces` | yes | Directory of 3D surface meshes in .vtk format, optionally with a color.json giving a colour per surface name. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `images` | `generic/images` | PNG renderings of the surfaces from six views, with an images.json index. |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `remove_background` | boolean | `true` | transparent background on the images |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.131](https://doi.org/10.25663/brainlife.app.131), choose `neuro/3Dsurfaces` from your project, set the parameters and press **Execute**. The results are saved to your project as `generic/images`.

### Locally

You need [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "surfaces": "/path/to/surfaces/surfaces",
       "remove_background": true
   }
   ```

3. Run `./main`.

## Troubleshooting

- **images missing**: Fewer PNGs were written than surfaces found; check the .vtk files and the rendering environment.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Plot 3D Surfaces. brainlife.io App. [doi:10.25663/brainlife.app.131](https://doi.org/10.25663/brainlife.app.131)
- Kitchell L. Shape Analysis of Human White Matter Tracts: An Examination of Normal Morphological Variability and the Association Between Morphology, Brain Size, and Behavior. Indiana University (2020).
- Kitchell, Lindsey. Shape Analysis of Human White Matter Tracts: An Examination of Normal Morphological Variability and the Association Between Morphology, Brain Size, and Behavior. Indiana University. 2020
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Lindsey Kitchell

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
