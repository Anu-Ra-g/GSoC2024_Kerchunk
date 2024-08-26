# Google Summer of Code 2024

**Organization:** [Integrated Ocean Observing System (IOOS)](https://summerofcode.withgoogle.com/programs/2024/organizations/ioos)  
**Contributor:** [Anurag Nayak](https://github.com/Anu-Ra-g)  
**Mentors:** [Martin Durant](https://github.com/martindurant)

## Faster NODD GRIB Aggregation

### Overview

[Kerchunk](https://fsspec.github.io/kerchunk/) is a python library that helps in providing a *unified* view a variety of chunked, compressed data formats (e.g. NetCDF/HDF5, GRIB2, TIFF, …) used for climate modelling purposes, from traditional file systems or cloud object storage.

The main aim of the project was to move the production code developed at **Camus Energy** to kerchunk library. This module was developed to work with `GRIB` files hosted by [NOAA NODD](https://www.noaa.gov/information-technology/open-data-dissemination) program. 

The workflow presented by this module significantly accelerates the process of handling GRIB files, which Kerchunk was originally designed for, reducing it to a fraction of the time. It was developed by [David Stuebe](https://github.com/emfdavid) as mentioned [here](https://github.com/asascience-open/nextgen-dmac/pull/57). 

The module works in a three step process as mentioned:

1. Extract and persist metadata directly from a few arbitrary grib files for a given product such as HRRR SUBH
2. Use the metadata mapping to build an index table of every grib message from the idx text files
3. Combine the index data with the metadata to build any FMRC slice (Horizon, RunTime, ValidTime, BestAvailable)

### Development Process. 

Before starting to code, I learnt the necessary tools and packages required for this project. This primarily includes [`kerchunk`](https://fsspec.github.io/kerchunk/), [`zarr`](https://zarr.readthedocs.io/en/stable/), [`xarray`](https://docs.xarray.dev/en/stable/), [`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/), [`xarray-datatree`](https://xarray-datatree.readthedocs.io/en/latest/) and [`pandas`](https://pandas.pydata.org/). Following this [video](https://www.youtube.com/watch?v=V0Xx0E8cs7U&t=655s) will give you a basic idea of what we're trying to deal with in this project. Apart from moving the functions from the module. 

