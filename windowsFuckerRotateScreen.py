import time
import rotatescreen

pd = rotatescreen.get_primary_display()
rotation = 0

time.sleep(50)

while True:
    for x in rotation:
        pd.rotate_to(x)
