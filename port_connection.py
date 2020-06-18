import wmi
from tkinter import *
import serial
import time
#global t1

def right():
    print("Moved right")
    bluetooth.write('a'.encode())
    #main_screen()
def forward():
    print("Moved Forward")
    bluetooth.write('f'.encode())
    #main_screen()
def backward():
    print("Moved Backward")
    bluetooth.write('d'.encode())
    #main_screen()
def moved():
    #stop function
    print("Stop")
    bluetooth.write('g'.encode())
    #main_screen()
    

def  left():
    bluetooth.write('s'.encode())
    print("butten")
    #main_screen()

def main_screen(x):
   global screen
   #print(x)
   screen = Tk()
   screen.geometry("800x450")
   screen.title("****ROBOTIC CAR REMOT SWITCH****")
   Label(text = "****ROBOTIC CAR REMOT SWITCH****",bg = "pink",width ="300", height = "2", font = ("Calibri",30)).pack()
   Label(text = "").pack()
   Button(text = "Left",height ="2", width ="30",bg = "Cyan",command = left).pack()
   Label(text = "").pack()
   Button(text = "Right" , height ="2", width ="30",bg = "blue",command = right).pack()
   Label(text = "").pack()
   Button(text = "BACKWARD",height ="2", width ="30",bg = "Yellow",command = forward).pack()
   Label(text = "").pack()
   Button(text = "FORWARD",height ="2", width ="30",bg = "Purple",command = backward).pack()
   Label(text = "").pack()
   Button(text = "STOP",height ="2", width ="30",bg = "Red",command = moved).pack()
   screen.mainloop()
c=wmi.WMI()
global m
wql="Select DeviceID from Win32_PnPEntity where name='HC-05'" #sal statement to retrive the data 
wql1="Select deviceid from win32_SerialPort"
global l1 # access from other function
l=[]
l1=[]
l3=[]

for item in c.query(wql):
    s=str(item)
    # this statement return the item present in the 
for item1 in c.query(wql1):
    l.append(item1)
serial1=str(l)
t=serial1.split('="')
for i in range(1,len(t)):
    serial3=str(t[i])
    l1.append(serial3[0:5])
#print(l1)

x=s.find("BLUETOOTHDEVICE")  # this stringg is used to find the com port in the serial communication
s=s[x+16:]

t=[]
for i in range(0,len(s)):
    if(s[i]=='"'):
        break
    else:
        t.append(s[i])

str1=""
m=str1.join(t)
#print(m)
wql3="Select PNPDeviceID from win32_SerialPort where deviceid='"
for i in range(0,len(l1)):
    
    wql4=wql3+l1[i]+str("'")
    l3.append(wql4)
for i in range(0,len(l3)):
    
    wql5=str(l3[i])
    
    for item7 in c.query(wql5):
        
        sfinder=str(item7)
        
        x2=sfinder.find(m)
        
        if(x2>1):
            print("sucess")
            global j
            j=i
            break
            #print(j)
t1=str(l1[j])

if(len(l1[j])>2):
    t=str(l1[j])
    print(t)
    bluetooth=serial.Serial(t1,9600)
    main_screen(t)
#this is the end of the programme

    
