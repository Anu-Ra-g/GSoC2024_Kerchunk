import fsspec
import s3fs

fs = fsspec.filesystem("s3", anon=True)

try:
    fs.get("s3://noaa-hrrr-bdp-pds/hrrr.20220804/conus/hrrr.t00z.wrfsfcf01.grib2", lpath="./")
except:
    pass

print("Downloading done")
