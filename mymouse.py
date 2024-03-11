import mouse
import time

ev = mouse.record()
print("repeat...begin.............")
while True:
    
    print("repeat................")
    mouse.play(ev)
    time.sleep(15)
