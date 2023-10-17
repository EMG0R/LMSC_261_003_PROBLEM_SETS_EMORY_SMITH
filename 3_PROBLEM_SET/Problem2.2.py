import math
in2 = input("please enter midi note to convert: ")
in2 = int(in2)
midinote = 2 ** ((in2 - 69) / 12) * 440
print("the frequency of midi",in2,"is:",midinote,".")