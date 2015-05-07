# -*- coding: utf-8 -*-

"""
Description
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import redis

__author__ = 'awang'

Base = declarative_base()


class Dao(object):
    """"""
    __db_uri = 'sqlite:///:memory:'  # 默认就是sqlite
    echo = True  # 如果是生存环境，可以改成False
    coding = 'utf-8'
    __rds_host = '127.0.0.1'
    __rds_port = 16379
    __rds_db = 1
    __session = None
    __redis = None

    @staticmethod
    def init_db_uri(env=None):
        """这里会重写一些数据库连接值"""
        db_type = 'mysql'
        db_user = 'root'
        db_host = '127.0.0.1'
        db_password = ''
        db_name = 'dyw'
        rds_host = '127.0.0.1'
        rds_port = 16379
        rds_db = 1
        Dao.__db_uri = '{}://{}:{}@{}/{}'.format(
            db_type, db_user, db_password, db_host, db_name)
        Dao.__rds_host = rds_host
        Dao.__rds_port = rds_port
        Dao.__rds_db = rds_db

    @staticmethod
    def engine():
        """:return sqlalchemy.create_engine"""
        return create_engine(Dao.__db_uri, echo=Dao.echo, encoding=Dao.coding)

    @staticmethod
    def session():
        """
        :return sqlalchemy.orm.Session
        """
        if Dao.__session is None:
            Dao.__session = Session(bind=Dao.engine())
        return Dao.__session

    @staticmethod
    def init_table_schema():
        """初始化表结构，默认只有单元测试的时候才用！*_*"""
        Base.metadata.create_all(bind=Dao.engine())

    @staticmethod
    def redis():
        """"""
        if Dao.__redis is None:
            Dao.__redis = redis.Redis(
                connection_pool=redis.ConnectionPool(
                    host=Dao.__rds_host,
                    port=Dao.__rds_port,
                    db=Dao.__rds_db
                )
            )
        return Dao.__redis

