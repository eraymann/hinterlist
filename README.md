# INTERLIS Tools Collection

## Purpose
This module contains tools 
* for checking interlis1 and interlis2 files by calling REST service.
* manipulate interlis1 files such as removing unused topics and tables

## Install
``pip install <path_to_your_wheel.whl>``

That's it.

## Version History
Version|Release Notes
---|---
0.0.1|Initial Version

## Examples
### Check Interlis 1 file

```python
# import module
from hinterlist import check

# Create instance of Checker with default server paths
mychecker = check.Checker()

# Submit synchroneous job, i.e. wait until check finished
result = mychecker.run_check(
    xtf=r"P:\ath\to\interlis1.itf",
    ili=r"P:\ath\to\model.ili",
    mode=check.Mode.SYNC,
    config=check.Config.ESRI
)

# Print results
print(result.jobid)
print(result.logfile)
print(result.success)
print(result.valid)

```
 ### Get Structure of Interlis 1 file
TODO