import pymel.core as pm

class NodeData(dict):
    NODE_DATA_ATTRIBUTE_NAME = 'nodeDataDict'
    def __init__(self, *args):
        node = [att for att in args if isinstance(att, (pm.PyNode, str))][0]
        dict_init = [att for att in args if isinstance(att, dict)]
        
        self.node = pm.PyNode(node)

        if dict_init:
            current_dict = dict_init[0]
        else:
            current_dict = eval(self._data_attribute.get())

        for k, v in current_dict.items():
            self.__setitem__(k,v)

    @property
    def _data_attribute(self):
        if not pm.attributeQuery(self.NODE_DATA_ATTRIBUTE_NAME, node=self.node, exists=True):
            pm.addAttr(self.node, dt='string', ln=self.NODE_DATA_ATTRIBUTE_NAME)
            self._data_attribute.set('{}')
            self._data_attribute.lock()

        return pm.Attribute('{}.{}'.format(self.node, self.NODE_DATA_ATTRIBUTE_NAME))

    def __getitem__(self, key):
        return eval(self._data_attribute.get())[key]

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
