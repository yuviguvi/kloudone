import os
import datetime

print("""

                       Alarm clock
          
             """)
date=input("present date=          ").split("-")
print("Present clock hour=")
print(datetime.datetime.today().strftime("                          %H"))
print("present clock minute=")
print(datetime.datetime.today().strftime("                          %M"))




Clockhour=int(input("Enter your Alarm hour=       "))


Clockminute=int(input("Enter your Alarm minute=     "))
while True:
    if Clockhour == int(datetime.datetime.today().strftime("%H")) and int(datetime.datetime.today().strftime("%M")):
        print("         wakeup!!")
        print("         wakeup!!")
        break
    else:
        print("exit")
input('\n\n press Enter to exit\n')




