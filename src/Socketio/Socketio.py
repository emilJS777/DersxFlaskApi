from .ISocketio import ISocketio
from src import socketio
from flask import request, g
from flask_socketio import send, emit, join_room
from src.Auth.AuthMiddleware import AuthMiddleware

sids: list = []


class Socketio(ISocketio):

    @socketio.on('connect')
    @AuthMiddleware.check_authorize
    def connect(self):
        sids.append({"sid": request.sid, "user_id": g.user_id})

    @socketio.on('disconnect')
    @staticmethod
    def disconnect():
        for sid in sids:
            if sid["sid"] == request.sid:
                sids.remove(sid)

    def send(self, emit_name: str, data: dict, user_id: int):
        for sid in sids:
            if sid['user_id'] == user_id:
                emit(emit_name, data, namespace=False, broadcast=True, to=sid["sid"])

    @socketio.on('get_online')
    @staticmethod
    def get_online(data: dict):
        print(data)
        for sid in sids:
            if sid["user_id"] == data['user_id']:
                emit('online', {'user_id': data['user_id']}, namespace=False, broadcast=True, to=request.sid)
                break
