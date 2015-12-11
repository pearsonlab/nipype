from .base import GraphPluginBase


class SGEGraphPlugin(GraphPluginBase):

    def __init__(self, **kwargs):
        super(SGEGraphPlugin, self).__init__(**kwargs)
