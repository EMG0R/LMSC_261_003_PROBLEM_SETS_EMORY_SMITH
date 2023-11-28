in4 = input("please enter song duration in minutes: ")
in4 = int(in4)
if in4 <= 2:
    print("this is a short song")
elif in4 < 4:
    print("this is a medium length song")
else:
    print("this is a long song")