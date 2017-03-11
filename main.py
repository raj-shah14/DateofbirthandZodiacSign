from datetime import date                           #Importing Library


count=0;

for count in range(0,3):
    #Taking input in given format
    DOB = input("Enter the date of birth in MM/DD/YYYY format\n")
    M,D,Y = DOB.split('/')
    M,D,Y=int(M),int(D),int(Y)
    if(Y<1800 or Y>2300):       #Checking for Validity of Year
        print("INVALID FORMAT!\n")
        count+=1
        continue
    elif(M<1 or M>12):          #Checking for Validity of Month
        print("INVALID FORMAT!\n")
        count+=1
        continue
    elif(D<1 or D>31):          #Checking for Validity of Day
        print("INVALID FORMAT\n")
        count+=1
        continue
    
    elif(M!=1 and M!=3 and M!=5 and M!=7 and M!=8 and M!=10 and M!=12):
        if(M==2):
                #Checking for Leap Year
            if (( Y%400 == 0)or (( Y%4 == 0 ) and ( Y%100 != 0))):
                
                if (D>29):
                      print("INVALID FORMAT\n")
                      count+=1
                      continue
                else:
                       break
            
            else:
               if (D>28):
                        print("INVALID FORMAT\n")
                        count+=1
                        continue  
            
               else:
                        break    
            
        else:
            if(D>30):
                print("INVALID FORMAT\n")
                count+=1
                continue
            else:
                break
    elif(M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12):
        if(D>31):
            print("INVALID FORMAT\n")
            count+=1
            continue
        else:
            break
    else:
       break
        
if(count==3):       
    print("Number of Input Attempts Exceeded")
    exit()
else:
    #Getting Day of the Week
    dow=(date(Y, M, D).weekday())
    if(dow==0):
        dow="MONDAY"
    elif(dow==1):
        dow="TUESDAY"
    elif(dow==2):
        dow="WEDNESDAY"
    elif(dow==3):
        dow="THURSDAY"
    elif(dow==4):
        dow="FRIDAY"
    elif(dow==5):
        dow="SATURDAY"
    else:
        dow="SUNDAY"
    print("Day on which you were born: " + dow + "\n")

    #Getting the Zodiac Sign
    if ((M==4 and (D>=19 and D<=30)) or (M==5 and (D>=1 and D<=13))):
        print ("Zodiac Sign: ARIES")
    if ((M==5 and (D>=14 and D<=31)) or (M==6 and (D>=1 and D<=19))):
        print ("Zodiac Sign: TAURUS")
    if ((M==6 and (D>=20 and D<=30)) or (M==7 and (D>=1 and D<=20))):
        print ("Zodiac Sign: GEMINI")
    if ((M==7 and (D>=21 and D<=31)) or (M==8 and (D>=1 and D<=9))):
        print ("Zodiac Sign: CANCER")
    if ((M==8 and (D>=10 and D<=31)) or (M==9 and (D>=1 and D<=15))):
        print ("Zodiac Sign: LEO")
    if ((M==9 and (D>=16 and D<=30)) or (M==10 and (D>=1 and D<=30))):
        print ("Zodiac Sign: VIRGO")
    if ((M==10 and (D==31)) or (M==11 and (D>=1 and D<=22))):
        print ("Zodiac Sign: LIBRA")
    if ((M==11 and (D>=23 and D<30))):
        print ("Zodiac Sign: SCORPIUS")
    if ((M==11 and (D==30)) or (M==12 and (D>=1 and D<=17))):
        print ("Zodiac Sign: OPHIUCHUS")
    if ((M==12 and (D>=18 and D<=31)) or (M==1 and (D>=1 and D<=18))):
        print ("Zodiac Sign: SAGITTARIUS")
    if ((M==1 and (D>=19 and D<=31)) or (M==2 and (D>=1 and D<=15))):
        print ("Zodiac Sign: CAPRICORNIS")
    if ((M==2 and (D>=16 and D<=29)) or (M==3 and (D>=1 and D<=11))):
        print ("Zodiac Sign: AQUARIUS")
    if ((M==3 and (D>=12 and D<=31)) or (M==4 and (D>=1 and D<=18))):
        print ("Zodiac Sign: PISCES")

