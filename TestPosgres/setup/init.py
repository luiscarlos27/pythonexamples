import sys
import os
import pandas as pd
import subprocess
import argparse
import pdb
import pickle
from setup_environment import *

engine = get_database()
try:
    con = engine.raw_connection()
    con.cursor().execute("SET SCHEMA '{}'".format('your_schema_name'))
except:
    pass
