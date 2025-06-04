import espnow
from wifi import Wifi

          
class Communication():
  def __init__(self, peer=False):
    self.is_wifi_conneted = Wifi.is_wifi_connected()
    self.peer = peer
    self.com = espnow.ESPNow()
    self.com.active(True)
    
  def _set_peer(self):
    if not self.peer:
      return False
    self.com.add_peer(self.peer)
    return True
    
  def sendMessage(self, message):
    if not self.is_wifi_connected:
      return {"status": "failed", "message":"Could not send message, no wifi connection"}
    if not self._set_peer():
      return {"status": "failed", "message": "Could not set peer"}
    self._set_peer()
    self.com.send(self.peer, message)
    print(f"Sent message: {message}")
    return {"status": "success", "message": "Message sent"}
    
    
        
  def recieve_message(self):
    if not self.is_wifi_connected:
      return {"status": "failed", "message":"Could not send message, no wifi connection"}
    host, msg = self.com.recv()
    if msg:             # msg == None if timeout in recv()
        print(host, msg)
        if msg == b'end':
            return {"status": "success", "message": "End of message"}
        return {"status": "success", "message": msg.decode('utf-8')}
    return {"status": "failed", "message": "No message received"}