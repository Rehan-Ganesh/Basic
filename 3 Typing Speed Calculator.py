from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error 

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)    
    speed = len(userinput)/ time_R
    return round(speed) 

while True:
    ck = input("ready to test ? : yes / no :")
    if ck == "yes":
     test=["Prepare to be enchanted by this exquisite home where classical aesthetics meet modern opulence Impeccably designed with premium finishes, this property is a masterpiece in every sense." 
      , "Ground floor Step into a generous 1245 sq.ft space, featuring a luxurious duplex living area, a chef's dream kitchen, and a versatile office space, ready to accommodate your professional needs.",
      "Third floor Ascend to a realm of serenity nd spirituality complete ith a grand puja room and a sophisticated study area. Additionally youll find a lavish master suite complete wh a walkin closet nd an exclusive balcony, offering a sanctuary r relaxation."]
     test1= r.choice(test)
     print("         *****typing speed*****    ")
     print(test1)
     print()
     print()
     time_1 = time()
     testinput= input("Enter: ")
     time_2 = time()

     print('Speed : ', speed_time(time_1, time_2, testinput)," w/sec")
     print("Error :", mistake(test1,testinput))
    elif ck == 'no' :
        print(" Thank you-Rehan_Ganesh Visit Again ")
        break
    else:
        print(" Wrong Input")

    
    

