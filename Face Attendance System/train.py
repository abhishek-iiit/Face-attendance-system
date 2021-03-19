#Importing the libraries
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import cv2,os
import csv
from PIL import Image,ImageTk
import datetime
import time

#***************************************************************************************
#Defining the Window
window = tk.Tk()
window.geometry('1485x867')
window.resizable(0, 0)
window.title("Attendance Portal @abhishek-iiit")
image=Image.open("_bg_.png")
photo=ImageTk.PhotoImage(image)
lab=tk.Label(image=photo,bg='#8fb5c2')
lab.pack()

#Defining the Labels
message = tk.Label(window, text="FACE ATTENDANCE PORTAL @abhishek-iiit" ,bg="#000000"  ,fg="green"  ,width=50  ,height=3,font=('Helvetica', 35, 'italic bold '))
message.place(x=60, y=20)

message = tk.Label(window, text="Note : ID must be Numeric & Name must be Alphabet without space." ,bg="#000000"  ,fg="red"  ,width=100  ,height=3,font=('Helvetica', 15, 'italic bold '))
message.place(x=100, y=480)

lbl = tk.Label(window, text="Enter ID :",width=20  ,height=2  ,fg="white"  ,bg="#000000" ,font=('Helvetica', 20 , ' bold ') ) 
lbl.place(x=100, y=200)
txt = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
txt.place(x=350, y=215)

lbl2 = tk.Label(window, text="Enter Name :",width=20  ,fg="white"  ,bg="#000000"    ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl2.place(x=100, y=300)
txt2 = tk.Entry(window,width=20  ,bg="white" ,fg="black",font=('Helvetica', 20 , ' bold '))
txt2.place(x=350, y=315)

lbl3 = tk.Label(window, text="Notification : ",width=20  ,fg="white"  ,bg="#000000"  ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl3.place(x=100, y=400)
message = tk.Label(window, text="" ,bg="grey"  ,fg="black"  ,width=40  ,height=2, activebackground = "yellow" ,font=('Helvetica', 20 , ' bold ')) 
message.place(x=350, y=400)

lbl3 = tk.Label(window, text="Attendance : ",width=20  ,fg="white"  ,bg="#000000"  ,height=2 ,font=('Helvetica', 20 , ' bold ')) 
lbl3.place(x=100, y=720)
message2 = tk.Label(window, text="" ,fg="black"   ,bg="grey",activeforeground = "green",width=50  ,height=2  ,font=('Helvetica', 20 , ' bold ')) 
message2.place(x=350, y=720)

#********************************************************************************************
def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            _ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                sampleNum=sampleNum+1
                cv2.imwrite("TrainingImage/ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
              
                cv2.imshow('frame',img)#display the frame 
            if cv2.waitKey(100) & 0xFF == ord('q'):#wait for 100 miliseconds 
                break
            elif sampleNum>60:# break if the sample number is morethan 60
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for: "+ name
        row = [Id , name]
        with open('StudentDetails/StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Enter Alphabetical Name"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    _detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("trainningData.yml")
    res = "Image Trained"
    message.configure(text= res)

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]#get the path of all the files in the folder 
    faces=[]#create empth face list
    Ids=[]#create empty ID list
    #loop through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')#loading the image and converting it to gray scale
        imageNp=np.array(pilImage,'uint8')#Now we are converting the PIL image into numpy array
        Id=int(os.path.split(imagePath)[-1].split(".")[1])#getting the Id from the image
        faces.append(imageNp)# extract the face from the training image sample
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainningData.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)  
    df=pd.read_csv("StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        _ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("./ImagesUnknown/Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(22, 123, 182),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Attendance/Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    message2.configure(text= res)

#Defining the Buttons**********************************************************************
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="red"  ,bg="white"  ,width=20  ,height=2 ,activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
clearButton.place(x=690, y=205)
clearButton2 = tk.Button(window, text="Clear", command=clear2  ,fg="red"  ,bg="white"  ,width=20  ,height=2, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
clearButton2.place(x=690, y=305)    
takeImg = tk.Button(window, text="Take Images", command=TakeImages  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
takeImg.place(x=100, y=610)
trainImg = tk.Button(window, text="Train Images", command=TrainImages  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
trainImg.place(x=400, y=610)
trackImg = tk.Button(window, text="Track Images", command=TrackImages  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
trackImg.place(x=700, y=610)
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg="red"  ,bg="white"  ,width=20  ,height=3, activebackground = "grey" ,font=('Helvetica', 15 , ' bold '))
quitWindow.place(x=1150, y=750)
 
window.mainloop()