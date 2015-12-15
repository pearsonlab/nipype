"""Parallel workflow execution via Spark
"""
import os
import sys
from .base import (PluginBase, logger)
from ...interfaces.base import CommandLine
from pyspark import SparkContext
sc = SparkContext()


class SparkPlugin(PluginBase):

    """Execute using Apache Spark

    The plugin_args input to run can be used to control the execution.
    Currently supported options are:
    -ADD OPTIONS HERE

    """

    def __init__(self, **kwargs):
        super(SparkPlugin, self).__init__(**kwargs)

    def run(self, flatgraph, execgraph, config):
        return

    def _submit_spark(self, pyfiles, execgraph, flatnodes):
        return
