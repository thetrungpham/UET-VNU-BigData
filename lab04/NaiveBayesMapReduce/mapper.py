import sys

for line in sys.stdin:
    outlook, temp, humidity, wind, playTennis = map(str, line.strip().split(','))

    print(f"(outlook,{outlook},{playTennis})\t1")
    print(f"(temp,{temp},{playTennis})\t1")
    print(f"(humidity,{humidity},{playTennis})\t1")
    print(f"(wind,{wind},{playTennis})\t1")
    print(f"(play,{playTennis})\t1")
