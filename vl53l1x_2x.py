# !/usr/bin/env python3

import pigpio # pigpioモジュールを使用
import time
# pigpioの準備
pi = pigpio.pi()

tof1_gpio = 17
tof2_gpio = 17

# GPIOピンを出力に設定
pi.set_mode(tof1_gpio, pigpio.OUTPUT)
pi.set_mode(tof2_gpio, pigpio.OUTPUT)

# I2Cの電源を切る
pi.write(tof1_gpio, 0)
pi.write(tof2_gpio, 0)

