# 自分のI2Cセンサーのプログラムをまとめとく場所
前提:ラズパイ
<hr><br>

# BMX055
- 9軸センサー(加速度3軸、ジャイロ3軸、磁気3軸)
- モノは[秋月](https://akizukidenshi.com/catalog/g/gK-13010/)
    - JP7をショートさせる(信号レベル電圧の問題)
- サードパーティーの公式リポジトリ [ControlEverythingCommunity/BMX055](https://github.com/ControlEverythingCommunity/BMX055/blob/master/Python/BMX055.py)
- 地磁気センサーはなんか動かなかったからコメントアウトしてる~どうせ使わないし~

# BMP280

- 気温・気圧(・標高)センサー
- モノは[aitendo](https://www.aitendo.com/product/15806) 青色基板
- SwitchScienceの公式リポジトリ [SWITCHSCIENCE/BME280](https://github.com/SWITCHSCIENCE/BME280)

# VL53L1X

- ToFレーザー距離センサー
- モノは[秋月](https://akizukidenshi.com/catalog/g/gM-12590)
- サードパーティーの[リポジトリ](https://github.com/pimoroni/vl53l1x-python)から
- https://team432.jpn.org/?p=380
- L1X!!L0じゃない!!4mはかれる方
<br>
- センサー2個使うとき
    - XSHUTで電源操作して、アドレス書き換え
    - `sudo gpio -g mode 27 out`でGPIOを出力モードに切り替え
    - `sudo gpio readall`で確認
    - `sudo gpio -g write 17 0`で電源オフ、`sudo gpio -g write 17 1`で電源オン