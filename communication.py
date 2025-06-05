import espnow
from wifi import Wifi

          
class Communication():
  def __init__(self, peer=None):
    self.is_wifi_conneted = Wifi.is_wifi_connected()
    self.peer = peer
    self.com = espnow.ESPNow()
    self.com.active(True)
    
  def get_peer(self):
    return self.peer
    
  def set_peer(self, peer=None):
    if peer:
      self.peer = peer
    self.com.add_peer(self.peer)
    return True
    
  def sendMessage(self, message):
    if not self.is_wifi_connected:
      return {"status": "failed", "message":"Could not send message, no wifi connection"}
    self.set_peer()
    self.com.send(self.peer, message)
    print(f"Sent message: {message}")
    return {"status": "success", "message": "Message sent"}
    
    
        
  def recieve_message(self):
    if not self.is_wifi_connected:
      return {"status": "failed", "message":"Could not send message, no wifi connection"}
    host, msg = self.com.recv()
    if msg:             # msg == None if timeout in recv()
        # "MOVE 500"
        print(host, msg)
        action = msg.split(" ")[0]
        step = msg.split(" ")[1]
        if msg == b'end':
            return {"status": "success", "message": [action, int(step)]}
        return {"status": "success", "message": msg.decode('utf-8')}
    return {"status": "failed", "message": "No message received"}