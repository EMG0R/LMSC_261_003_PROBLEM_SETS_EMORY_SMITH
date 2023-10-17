in1 = input("please enter song duration in seconds: ")
int1 = int(in1)
min1 = int(int1) // int(60)
sec1 = int1 % 60
print("the song is ", min1, " minutes and ", sec1, " seconds.")