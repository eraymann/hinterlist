# INTERLIS Tools Collection

## Purpose
This module contains tools 
* for checking interlis1 and interlis2 files by calling REST service.
* manipulate interlis1 files such as removing unused topics and tables

## Install
``pip install hinterlist``  

That's it.

## Version History
Version|Release Notes
---|---
0.0.4|error count in result
0.0.3|server alias as optional parameter
0.0.2|detox submodule added
0.0.1|initial version

## Examples
### Check Interlis 1 file

```python
# import module
from hinterlist import check

# create instance of Checker with default server paths
mychecker = check.Checker(server="gugus.dada.admin.ch:6443")

# submit synchroneous job, i.e. wait until check finished
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
print(result.errors)

```
 ### Get Structure of Interlis 1 file
TODO