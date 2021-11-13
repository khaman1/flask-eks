from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Boolean, text, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker, validates
from .sql_alchemy import mySQLAlchemy
from datetime import datetime
import os
import sys
from .funcs import *
from urllib.parse import quote


def new_engine():
    return create_engine('postgresql://root:root@postgres-srv:5432/postgres', pool_pre_ping=True, pool_recycle=600)
