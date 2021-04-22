#!/bin/python
import yaml
from flask import Flask, request

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


