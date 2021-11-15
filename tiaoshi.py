# -*- encoding=utf8 -*-
__author__ = "zhoupeng03"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["Android:9HUKPVLJ4DGQ4HSS",])


# script content
print("start...")

start_app('cn.jj.log')
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
