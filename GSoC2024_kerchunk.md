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

1. Extract and persist metadata directly from a few arbitrary grib files for a given product such as HRRR SUBH, GEFS, GFS etc. 
2. Use the metadata mapping to build an index table of every grib message from the `idx` text files
3. Combine the index data with the metadata to build any FMRC slice (Horizon, RunTime, ValidTime, BestAvailable)

### Development Process. 

Before starting to code, I learnt the necessary tools and packages required for this project. This primarily includes [`kerchunk`](https://fsspec.github.io/kerchunk/), [`zarr`](https://zarr.readthedocs.io/en/stable/), [`xarray`](https://docs.xarray.dev/en/stable/), [`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/), [`xarray-datatree`](https://xarray-datatree.readthedocs.io/en/latest/) and [`pandas`](https://pandas.pydata.org/). Following this [video](https://www.youtube.com/watch?v=V0Xx0E8cs7U&t=655s) will give you a basic idea of what we're trying to deal with in this project. In addition to above methods and learning, I explored how `kerchunk` is used with the help of materials in [**Project Pythia**](https://projectpythia.org/). The [foundations](https://foundations.projectpythia.org/landing-page.html) and [kerchunk cookbook](https://foundations.projectpythia.org/landing-page.html) sections in it contains most of the material that you need to get started 

Apart from moving the code to kerchunk's API, other tasks that was involved in the project were:

* Make the functions in the API compatible with the GRIB files on **AWS**.
* Write the unit tests for the functions and develop tests to evaluate the workflow.
* Make the new notebooks with the aggregation workflow and other implementations.
* Ensure that the implementation adheres to clean code principles.
* Add a page to kerchunk's documentation for this new approach.  

### Code example

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>varname</th>
      <th>typeOfLevel</th>
      <th>stepType</th>
      <th>name</th>
      <th>step</th>
      <th>level</th>
      <th>time</th>
      <th>valid_time</th>
      <th>uri</th>
      <th>offset</th>
      <th>length</th>
      <th>inline_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>gh</td>
      <td>isobaricInhPa</td>
      <td>instant</td>
      <td>Geopotential height</td>
      <td>0 days 06:00:00</td>
      <td>0.0</td>
      <td>2017-01-01 06:00:00</td>
      <td>2017-01-01 12:00:00</td>
      <td>s3://noaa-gefs-pds/gefs.20170101/06/gec00.t06z...</td>
      <td>0</td>
      <td>47493</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>t</td>
      <td>isobaricInhPa</td>
      <td>instant</td>
      <td>Temperature</td>
      <td>0 days 06:00:00</td>
      <td>0.0</td>
      <td>2017-01-01 06:00:00</td>
      <td>2017-01-01 12:00:00</td>
      <td>s3://noaa-gefs-pds/gefs.20170101/06/gec00.t06z...</td>
      <td>47493</td>
      <td>19438</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>r</td>
      <td>isobaricInhPa</td>
      <td>instant</td>
      <td>Relative humidity</td>
      <td>0 days 06:00:00</td>
      <td>0.0</td>
      <td>2017-01-01 06:00:00</td>
      <td>2017-01-01 12:00:00</td>
      <td>s3://noaa-gefs-pds/gefs.20170101/06/gec00.t06z...</td>
      <td>66931</td>
      <td>10835</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>u</td>
      <td>isobaricInhPa</td>
      <td>instant</td>
      <td>U component of wind</td>
      <td>0 days 06:00:00</td>
      <td>0.0</td>
      <td>2017-01-01 06:00:00</td>
      <td>2017-01-01 12:00:00</td>
      <td>s3://noaa-gefs-pds/gefs.20170101/06/gec00.t06z...</td>
      <td>77766</td>
      <td>22625</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>v</td>
      <td>isobaricInhPa</td>
      <td>instant</td>
      <td>V component of wind</td>
      <td>0 days 06:00:00</td>
      <td>0.0</td>
      <td>2017-01-01 06:00:00</td>
      <td>2017-01-01 12:00:00</td>
      <td>s3://noaa-gefs-pds/gefs.20170101/06/gec00.t06z...</td>
      <td>100391</td>
      <td>20488</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>

> Note: *The above is the index created for a single GRIB file*

#### What's done

---

* Moved most of the functions from the original codebase to `kerchunk`.
* Wrote the unit tests for those functions.
* Added a new notebook to **Project Pythia** for this operation.
* Tested out the workflow with **GEFS**, **GFS** and **HRRR** data

#### What's next

--- 

* Implement the creation of `.idx` files for the respective grib files locally.
* Figure out a way to create references for nested grib messages.

#### Notebook's created
* [Testing the index](https://gist.github.com/Anu-Ra-g/efa01ad1c274c1bd1c14ee01666caa77)
* [Workflow with GEFS](https://gist.github.com/Anu-Ra-g/e0d7b9c815dcd4df4ea2261ed272e5d3)


[My Pull Requests](https://github.com/fsspec/kerchunk/pulls?q=is%3Apr+is%3Aclosed+author%3AAnu-Ra-g)

Pull requests associated with the project:

* Added documentation for `kerchunk` as a backend in `xarray` [#9163](https://github.com/pydata/xarray/pull/9163)
* Updated the hook for `nbqa` to support the new version of `ruff`[#862](https://github.com/nbQA-dev/nbQA/pull/862)
* Updated the pre-commit configuration for Project Pythia [#63](https://github.com/ProjectPythia/kerchunk-cookbook/pull/63)