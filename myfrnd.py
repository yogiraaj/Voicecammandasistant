import os
import typing
#import openai
import pyttsx3
import speech_recognition as sr
import datetime
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pyautogui
import time
from PyQt5 import QtWidgets , QtCore , QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from myfrndgui import Ui_leoGui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)  #voice change id

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#for wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")

    elif hour>12 and hour<18:
        speak(f"good afternood, its {tt}")
    else:
        speak(f"jai shree ram, its {tt}")
    speak("I am leo. what can i do for you?")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id' ,to,content)
    server.close()


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
    def run(self):
        self.TaskExecution()
        
        


    #voice to text
    def takecommand(self):  
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #audio = r.listen(source,timeout=5,phrase_time_limit=8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            #speak("say that again please...")
            return "none"
        
        return query



    def TaskExecution(self):
        wish()
        while True:
            if 1:
        

                self.query = self.takecommand().lower()

            #working tasks

                if "open notepad" in self.query:
                    npath= "C:\\Windows\\notepad.exe"
                    os.startfile(npath)


                elif "close notepad" in self.query:
                    speak("okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")

            
                elif "open command prompt" in self.query:
                    os.system("start cmd")

                elif "close command prompt" in self.query:
                    speak("okay sir, closing command prompt")
                    os.system("taskkill /f /im cmd.exe")
        
                elif "open camera" in self.query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read(0)
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif "close camera" in self.query:
                    speak("okay sir, closing camera")
                    pyautogui.press("esc")

        # elif "play music on spotify" in query:
            #    apath= 

                elif "ip address" in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your ip address is {ip}")

                elif "wikipedia" in self.query:
                    speak("searching on wikipedia...")
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences = 3)
                    speak("according to wikipedia")
                    speak(results)
                    print(results)

                elif "open youtube" in self.query:
                    webbrowser.open("youtube.com")

                elif "open facebook" in self.query:
                    webbrowser.open("facebook.com")

                elif "open wikipedia" in self.query:
                    webbrowser.open("wikipedia.com")

                elif "open google" in self.query:
                    speak("sir, what should i search on google")
                    cm = self.takecommand()
                    webbrowser.open(f"{cm}")

                elif "send message" in self.query:
                    kit.sendwhatmsg("+9619713720", "this is testing protocal",1,10)

                
                elif "play song on youtube" in self.query:
                    kit.playonyt("arjit singh playlist")

                elif "email to yogi" in self.query:
                    try:
                        speak("what should i say")
                        content = self.takecommand().lower()
                        to = "yogeshpal2005@gmail.com"
                        smtplib(to,content)
                        speak("Email has been sent to yogi")

                    except Exception as e:
                        print(e)
                        speak("sorry sir,because of network issue i am not able to sent mail to yogi")

            

            

                elif "tell me a joke" in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "shut down the system" in self.query:
                    os.system("shutdown /s/t 5")

                elif "restart the system" in self.query:
                    os.system("shutdown/r/t 5")

                elif "sleep the system" in self.query:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                elif "switch window" in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                #ss
                elif "take screenshot" in self.query or "screenshot" in self.query:
                    speak("sir, tell me the name of the screenshot file")
                    name = self.takecommand().lower()
                    speak("please hold a second, i am taking screenshot")
                    time.sleep(2)
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

                #to check insta profile

                elif "check profile on instagram" in self.query or "instagram" in self.query:
                    speak("Enter instagram id correctly")
                    name = input("Enter user name here")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak("sir here is the profile of the user {name}")
                    time.sleep(2)

                #location
                elif "where i am" in self.query or "find my location" in self.query:
                    speak("wait sir, let me check")
                    try:
                        ipAdd = get.requests('https://api.ipify.org').text
                        print(ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                        geo_requests = get.requests(url)
                        geo_data = geo_requests.json()
                        city = geo_data['city']
                        state = geo_data['state']
                        country = geo_data['country'] 
                        speak(f"i am not sure, but i think we are in {city} city of {state} state in{country}")
                    except Exception as e:
                        speak("sorry sir, due to network issue i am not able to find where we are")
                        pass              


                elif "you can sleep" in self.query:
                    speak("thank you sir , have a good day")
                    sys.exit()


                #speak("sir, what can i do")
                

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_leoGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.openLink)

    def openLink(self):
        
        url = QUrl("https://speechto2text.netlify.app")
        QDesktopServices.openUrl(url)
               
        


    def startTask(self):
        self.ui.movie = QtGui.QMovie("New folder/Glow Matrix - Animated.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("New folder/initiating.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("New folder/loading_1.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
leo = Main()
leo.show()
exit(app.exec_())




        


    

