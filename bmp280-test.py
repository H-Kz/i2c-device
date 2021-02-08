import time
time_start = time.time()
import bmp280
data=bmp280.readData()
print(data)
print("所要時間 "+str(time.time()-time_start))
