import pymel.core as pm

class NodeData(dict):
    NODE_DATA_ATTRIBUTE_NAME = 'nodeDataDict'
    def __init__(self, *args, **kwargs):
        node = [arg for arg in args if isinstance(arg, (pm.PyNode, str))][0]
        dict_init = [arg for arg in args if isinstance(arg, dict)]
        
        self.node = pm.PyNode(node)

        if dict_init:
            current_dict = dict_init[0]
        else:
            current_dict = eval(self._data_attribute.get())

        self.update(current_dict)

    @property
    def _data_attribute(self):
        if not pm.attributeQuery(self.NODE_DATA_ATTRIBUTE_NAME, node=self.node, exists=True):
            pm.addAttr(self.node, dt='string', ln=self.NODE_DATA_ATTRIBUTE_NAME)
            self._data_attribute.set('{}')
            self._data_attribute.lock()

        return pm.Attribute('{}.{}'.format(self.node, self.NODE_DATA_ATTRIBUTE_NAME))

    def __getitem__(self, key):
        self._setNodeAttribute()
        return self[key]

    def __setitem__(self, key, value):
        super(NodeData, self).__setitem__(key, value)
        self._setNodeAttribute()
        
    def __delitem__(self, key):
        super(NodeData, self).__delitem__(key)
        self._setNodeAttribute()

    def _setNodeAttribute(self):
        self._data_attribute.unlock()
        self._data_attribute.set(self.__str__())
        self._data_attribute.lock()
        
    def clear(self):
        super(NodeData, self).clear()
        self._setNodeAttribute()
        
    def update(self, *args, **kwargs):
        super(NodeData, self).update(*args, **kwargs)
        self._setNodeAttribute()
