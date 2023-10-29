from camera import Camera
from ui import MainMenu

url = "http://192.168.242.18:8080/shot.jpg"

cam = Camera(url)

MainMenu(cam)
