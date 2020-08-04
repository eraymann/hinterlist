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
from hinterlist import checker

# Create instance of Checker with default swisstopo ETL prod server paths:
mychecker = checker.Checker()

# Submit synchroneous job, d.h. wait until check finished
result = mychecker.run_check(
    xtf=r"P:\ath\to\interlis1.itf",
    ili=r"P:\ath\to\model.ili",
    mode=checker.Mode.SYNC,
    config=checker.Config.ESRI
)

# Print results
print(result.jobid)
print(result.logfile)
print(result.success)
print(result.valid)

```
