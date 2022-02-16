# WRFtamer
WRFtamer is a tool to organize WRF simulations. This includes organizing experiments into projects, creating simulations, running WPS, postprocessing data and archiving completed runs. This tool also provides an overview on how long a simulation runs and how much disk space it takes. 
The programm can be used from the command line and using a graphical user interface (GUI).
WRFtamer is designed to run WRF with em_real. Is is able to create sumbit-scripts for the cluster, but only for the SLURM job scheduler. 

## Requirements
This repository has been tested with python 3.7.12
### External python modules
- click
- numpy
- pathlib
- netCDF4
- pandas
- tqdm
- matplotlib
- pyyaml
- xarray
- cartopy
- shapely
- pytest
- panel 
- openpyxl
  
## Installation
It can be installed with 
```bash
python setup.py install
```
If you do so, don't forget to reinstall after any changes.
During development, a better way is to install using editable mode with pip:
```bash
pip install -e .
```

## First Steps and documentation

For first steps to use WRFtamer go to <link1>.

The full documentation is available at <link2>. 

Links will be put here as soon as the webpage is online.  

## Repo Structure
```bash
├── bash # shell scripts for some of the options
├── scripts # main file with all options
├── tests # test script for this repository
├── resources # all resources that are used by the tests
├── wrftamer # python scripts for some of the options
├── resources # templates for the namelist and the config-file 
├── documentation  # documentaion using mkdocs 
```
## Conventions
Python programs should fulfill pep8 standard.
## Owners
Linda Menger, Daniel Leukauf
## Licence
TBA