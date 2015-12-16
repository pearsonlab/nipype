"""Parallel workflow execution via Spark
"""
import sys,re,os
from .base import (PluginBase, logger,create_pyscript)
from nipype.pipeline.engine import JoinNode, MapNode, Node
from nipype.utils.filemanip import loadpkl
from ...interfaces.base import CommandLine
from pyspark import SparkContext
import networkx as nx
from collections import OrderedDict
sc = SparkContext()


class SparkPlugin(PluginBase):

    """Execute using Apache Spark

    The plugin_args input to run can be used to control the execution.
    Currently supported options are:
    -ADD OPTIONS HERE

    """

    def __init__(self, **kwargs):
        super(SparkPlugin, self).__init__(**kwargs)

    def run(self, flatgraph, execgraph, config,updatehash=False):
        self._config = config
        logger.debug('Creating executable python files for each node')
        nodes = OrderedDict()
        for node in nx.topological_sort(flatgraph):
            execnodes = [i for i in execgraph.nodes() if node.name==i.name]
            pyfiles = [create_pyscript(i) for i in execnodes]
            nodes[node] = pyfiles
        _submit_spark(nodes,execgraph)

    def _submit_spark(self, nodes, execgraph):
        rdd = sc.parallelize(nodes.values[0])
        broadcast_graph = sc.broadcast(execgraph)
        for node in nodes:
            #Make sure contents of RDD are what we think they are by checking against nodes[node]

            #This is just a sketch of this...
            if node.iterables:
                rdd = rdd.flatMap(execIterables)
            elif isinstance(node,JoinNode):
                rdd = rdd.reduce(execJoinNode)
            elif isinstance(node,MapNode):
                rdd = rdd.flatMap(execMapNode)
            else:
                rdd = rdd.map(execNode)

    def execNode(pyfile):
        pyscript = open(pyfile).read()
        pkl_file = re.findall(r"pklfile = '(.*pklz)'",pyscript)[0]
        info = loadpkl(pkl_file)
        exec(pyscript)
        return broadcast_graph.value.successors(info['node'])

    def execJoinNode(pyfile):
        return

    def execMapNode(pyfile):
        return

    def execIterables(pyfile):
        return
    
    
