'''
Created on Apr 7, 2014

@author: TuanNA
'''
from tornado import websocket


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")
    def on_message(self, message):
        self.write_message(u"You said: " + message)
    def on_close(self):
        print("WebSocket closed")