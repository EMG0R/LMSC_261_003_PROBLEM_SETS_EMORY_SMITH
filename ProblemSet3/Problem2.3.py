in3 = input("please enter BPM to convert: ")
in3 = int(in3)
bpm = float(60000 / in3)
print("A quarter note delay in milliseconds for",in3,"BPM is",bpm,"ms.")