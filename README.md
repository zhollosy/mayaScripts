# mayaScripts
Python scripts for Autodesk Maya

# [NodeData.py](/NodeData.py)
Stores information in the node's string attribute. Helps adding and removing stored data.

Initialize with a dictionary:
```
d = {'asd': 3123, '33': 'sdfsd'}
ddd = NodeData('pSphereShape1', d)
```

Add/delete keys:
```
aa = NodeData('pSphereShape1')
aa['aa'] = 11
aa['bb'] = 22
del aa['aa']
```
