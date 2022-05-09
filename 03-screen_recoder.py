# Importing refers to allowing a Python file or a Python module to access the script from another Python file or module.
# capture photoes continuously to capture video
import cv2, pyautogui, numpy as np,time
from win32api import GetSystemMetrics
w=GetSystemMetrics(0) # width
h=GetSystemMetrics(1) # height
d=(w,h)
a=cv2.VideoWriter_fourcc(*'XVID') # this is input. XVID captures the video
o=cv2.VideoWriter('04-py_screen-recoder.mp4',a,30,d) # 30 is frame/sec o=output 
st=time.time() # start time
dur=35 # duration in sec
et=st+dur # end time
while True:
    i=pyautogui.screenshot() # pyautogui take screenshot
    f=np.array(i)
    f2=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    o.write(f2)
    c_time=time.time()
    if c_time > et:
        break
o.release()
print('---Screen Capturing Done---')





