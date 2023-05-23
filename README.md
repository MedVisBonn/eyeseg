# eyeseg
eyeseg is a command line application to segment OCT layers and quantify drusen. It can read and process Spectralis XML and VOL exports. Models used for OCT layer segmentation might give unexpected results on data from other devices than Spectralis.

## Installation
You can install `eyeseg` with pip. Use a virtual environment to avoid conflicts with other packages.

```bash
pip install eyesegpy
```

For GPU access you might have to install additional dependencies such as the CUDA Toolkit and cuDNN. Predictions using only the CPU are possible but a lot slower. A convenient alternative to installing additional depencies is to use our docker image. See the section "Docker" for more information.

### Docker
You can build the docker image yourself using the Makefile in the `docker/` folder or use the prebuild images on [Docker Hub](https://hub.docker.com/r/olcifer/eyeseg).

#### Build docker image
```bash
cd docker
make build_gpu
```

#### Run docker image

Running eyeseg in a docker container on mounted data only requires a working docker installation. You need nvidia-docker2 for GPU support which sigificantly speeds up segmentations. For more information on how to install docker and nvidia-docker2, please refer to the [docker documentation](https://docs.docker.com/install/).

For CPU only support, you can use the CPU image:
```bash
docker run -u $(id -u):$(id -g) -it -v $(DATA):/home/data olcifer/eyeseg:0.3.0-cpu
```
For GPU support, you can use the GPU image:
```bash
docker run -u $(id -u):$(id -g) -it --gpus=all -v $(DATA):/home/data olcifer/eyeseg:0.3.0-gpu
```

In both cases you need to mount your data to the container by replacing $(DATA) with the path to your data. Depending on whether you want to use a prebuild image or not you have to adapt the image name. The container will run as the current user and group. This is important to avoid permission issues with the mounted data. Your working directory is your mounted data.

## Requirements
Your data has to be in the Spectralis XML or VOL export format. In case of the XML export, make sure that your data is exported with a black background and every folder contains a single volume (single XML file). There is also a model available for Bioptigen data, trained on the Duke dataset. However, Biotigen data is not that common and the model is here mainly for reproducibility of the results described in the respective publication (https://doi.org/10.1038/s41598-023-35230-4).

## Usage
After installation via pip or starting the docker container, you can use the eyeseg command line application. You can run `eyeseg` without any arguments to see a help message.

### Available commands
`eyeseg` provides the following commands all with their own help message for more information:

* `eyeseg check` - check mounted data for common problems such as inverted contrast and multiple exports per directory (only XML)
* `eyeseg segment` - Segment OCT layers, compute drusen and save results as .eye files
* `eyeseg quantify` - Quantify drusen from .eye files and save results as .csv file
* `eyeseg plot-enface` - Plot enface images with drusen segmentation overlay
* `eyeseg plot-bscans` - Plot B-scans with layer/drusen segmentation overlay


## Examples
### Check data

```bash
eyeseg check
```

### Segmentation with default drusen threshold

```bash
eyeseg segment -t 2
```

The output is saved as a .eye file in the specified output folder (processed/ by default). The .eye file contains layer heights and drusen segmentation. The drusen segmentation is computed with a default threshold of 2. You can change the threshold with the `-t` option.

### Quantification with default grid

```bash
eyeseg quantify -r 0.8 -r 1.8 -s 1 -s 4 -o 0 -o 45
```

Drusen results are saved in the output folder as `drusen_results.csv`. You can change the quantification grid with the `-r`, `-s` and `-o` options.

### Plot enface overviews
Plot the localizer image with drusen overlay. Also add a rectangle for the B-scan area and lines indicating B-scan positions.

```bash
eyeseg plot-enface --drusen --bscan-area -p 52
```

The output is saved as a .jpeg file in the specified output folder (processed/ by default). An example eneface for the command above based on our models prediction is shown below.
![Enface overview](/docs/example_enface_52.jpeg)
The B-scan area is marked with a rectangle and the B-scan position of the 52th B-scan is marked with a line. The drusen segmentation is shown as a red overlay and the scale is in pixels.

### Plot B-scans
Plot bscans for the volumes indicated by the -v option. Without this option B-scans for all available volumes are plotted. If you want to plot predicted layers specify them with the -l option. By default no layers are plotted.

```bash
eyeseg plot-bscans --drusen -l BM -l RPE -v volume_name -v volume_name2
```

The output is saved as a .jpeg files in the specified output folder (processed/ by default). An example bscan for the command above based on our models prediction is shown below. It is the 52th B-scan of the same volume as in the example above.
![Bscan](/docs/example_bscan_52.jpeg)

## The quantification grid
Drusen quantification is performed on a circular grid centered on the localizer image. The grid is scaled according to the respective volumes scales provided in the meta data and flipped according to the laterality.

Arbitrary grids can be configured:
+ Specify the ring radii in ascending order in [mm] with the `-r` option.
+ Specify the respective number of sectors per ring with the `-s` option.
+ Specify the angular offset from the horizontal line in each ring in degree with the `-o` option.

By default the first sector starts on the nasal side from the horizontal line and subsequent sectors are added counter-clockwise for OD volumes and clockwise for OS volumes. See examples below:

+ Quantification grids for parameters `-r 1 -r 2 -s 1 -s 4 -o 0 -o 45`

![](./docs/grid1.jpeg)

+ Quantification grids for parameters `-r 1 -r 2 -r 3 -s 1 -s 4 -s 8 -o 0 -o 45, -o 45`

![](./docs/grid2.jpeg)
## Citation

```bibtex
@article{morelleAccurateDrusenSegmentation2023,
  title = {Accurate Drusen Segmentation in Optical Coherence Tomography via Order-Constrained Regression of Retinal Layer Heights},
  author = {Morelle, Olivier and Wintergerst, Maximilian W. M. and Finger, Robert P. and Schultz, Thomas},
  date = {2023-05-19},
  journaltitle = {Scientific Reports},
  shortjournal = {Sci Rep},
  volume = {13},
  number = {8162},
  publisher = {{Nature Publishing Group}},
  issn = {2045-2322},
  doi = {10.1038/s41598-023-35230-4},
  issue = {1},
  langid = {english},
  keywords = {Biomarkers,Computational science,Computer science,Macular degeneration},}
}
```
