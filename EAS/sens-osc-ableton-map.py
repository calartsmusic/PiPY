import time
from gpiozero import MCP3008
from gpiozero import Button
from pythonosc import udp_client

pc = MCP3008(0)
pot1 = MCP3008(1)
pot2 = MCP3008(2)
button1 = Button(17)
button2 = Button(27)

ip = "192.168.0.108"
port = 5000

client = udp_client.SimpleUDPClient(ip, port)

while True:
    client.send_message("/photocell", pc.value)
    time.sleep(5)
    client.send_message("/pot1", pot1.value)
    time.sleep(5)
    client.send_message("/but1", button1.value)
    time.sleep(5)
    client.send_message("/but2", button2.value)
    time.sleep(.02)
