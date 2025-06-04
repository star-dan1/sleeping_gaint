import network
import time



class Wifi:
    def __init__(self):
        self.is_connected = False
        self.wlan = network.WLAN()
        self.wlan.active(True)
        

    def connect_to_wifi(self, ssid, key, timeout=10):
        try:
            self.wlan.connect(ssid, key)
            for _ in range(timeout):
                if self.wlan.isconnected():
                    self.is_connected = True
                    return
                time.sleep(1)
            print("Connection timed out")
            self.is_connected = False
        except OSError as e:
            print(e)
            self.is_connected = False

    def is_wifi_connected(self):
        return self.is_connected

    def scan(self):
        return self.wlan.scan()

    
wifi = Wifi()
# print(wifi.scan())
all_wifi =  wifi.scan()
for wifi_name in all_wifi:
    print(wifi_name[0])
wifi.connect_to_wifi("ESP AP", "Daniel123")
print(wifi.is_wifi_connected())


# import network

# ap = network.WLAN(network.WLAN.IF_AP)
# ap.config(ssid = 'ESP AP')
# ap.config(max_clients=10)
# ap.active(True)

