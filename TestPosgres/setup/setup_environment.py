#!/usr/bin/env python
import os
import yaml
from sqlalchemy import create_engine
import logging

log = logging.getLogger(__name__)

def get_database():
    try:
        engine = get_connection()
        log.info("Connected to DB!")
    except IOError:
        log.exception("Failed to get DB!")
        return None, 'fail'

    return engine


def get_connection(config_file="../config/postgres.database.yaml"):
    with open(config_file,'r') as f:
        vals = yaml.load(f)

    if not ('production' in vals.keys()):
        raise Exception('Bad config file: ' + config_file)

    return get_engine(vals['development']['database'], vals['development']['username'],
                      vals['development']['host'], vals['development']['port'],
                      vals['development']['password'],vals['development']['pool'])

def get_engine(db, user, host, port, passwd,pool):
    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=user, passwd=passwd, host=host, port=port, db=db)
    engine = create_engine(url, pool_size = pool)
    return engine
