from .config import app, db, logger, api, socketio
from .routes import *
# from kink import di
from .Socketio import ISocketio, Socketio

#
# class InjectConfig:
#     @staticmethod
#     def setup():
#         di.factories[ISocketio.ISocketio] = lambda di: Socketio.Socketio()
