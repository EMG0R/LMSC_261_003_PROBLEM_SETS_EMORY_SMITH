import time
in51 = input("please enter song tempo: ")
in51 = int(in51)
in51 /= 60
in52 = input("please enter song length in seconds: ")
in52 = int(in52)
timecount = 0
beatcount = 0
while timecount < in52:
    print("at",timecount,"seconds,",beatcount,"beats")
    timecount += 1
    beatcount += in51