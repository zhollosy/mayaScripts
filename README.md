# mayaScripts
Python scripts for Autodesk Maya :+1:

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

Update dictionary:
```
d = {'asd': 3123, '33': 'sdfsd'}
d2 = {'asdd': 31223, '332': 'sdfsdxxx'}

ddd = NodeData('pCircle1Shape', d)
ddd.update(d2)
```
