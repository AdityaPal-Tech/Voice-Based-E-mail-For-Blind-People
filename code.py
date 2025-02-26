import speech_recognition as sr
import smtplib
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os
import time
from email.header import decode_header
def speak (t):
    say= gTTS(text= t, lang='en')

    convert=("1.mp3")
    say.save(convert)
    music = pyglet.media.load(convert, streaming = False)
    music.play()
    time.sleep(music.duration)
    os.remove(convert)  
ans="yes"
while ans=="yes":
    print ("*Welcome to Voice Based Email\nPlease enter your username\n")
    ##say= gTTS(text=" Hi welcome to voice based email system , please enter your email username   \n", lang='en')
    ##convert=("1.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()
    ##time.sleep(music.duration)
    ##os.remove(convert)
    speak("hi welcome to voice based email system ,please enter your email username")

    speech1 = sr.Recognizer()
    with sr.Microphone() as source:
        speech1.adjust_for_ambient_noise(source,duration=1)
        print ("\tYour email :\n")
        speech2=speech1.listen(source)
        print ("\t\t\tCommand Accepted\n")

    try:
        email_1=((speech1.recognize_google(speech2)).replace(" ", "")).lower()
        email_id = email_1 + "@gmail.com"
        print ("\t\tYou said : "+email_id)
        speak("You said : "+email_id)
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again")
         
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))


    print ("Please enter your password \n")
    ##say= gTTS(text="  please enter your password   \n", lang='en')
    ##convert=("2.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()
    ##time.sleep(music.duration)
    ##os.remove(convert)
    speak("please enter your password")
    speech3 = sr.Recognizer()
    with sr.Microphone() as source:
        speech3.adjust_for_ambient_noise(source,duration=1)
        print ("\tYour password :\n")
        speech4=speech3.listen(source)
        print ("\t\t\tCommand Accepted\n")

    try:
        password=((speech3.recognize_google(speech4)).replace(" ", "")).lower()
        print ("\t\tYou said : "+password)
        speak("you said "+password)
       
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again")
         
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))

    print ("please enter your choice ")
    ##say = gTTS(text="please enter your desired choice ", lang='en')
    ##convert=("start2.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()    
    ##time.sleep(music.duration)
    ##os.remove(convert)
    speak("please enter your desired choice ")



    print ("\t\t\t1. compose a mail. \t\t\t\t\t\t\n")
    ##say = gTTS(text="Say 'compose' to compose a mail.", lang='en')
    ##convert=("start2.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()    
    ##time.sleep(music.duration)
    ##os.remove(convert)
    speak("Say 'compose' to compose a mail.")



    print ("\t\t\t2. Check your inbox. \t\t\t\t\t\n")
    ##say= gTTS(text="Say 'check' to Check your inbox", lang='en')
    ##convert=("start2.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()    
    ##time.sleep(music.duration)
    ##os.remove(convert)
    speak("Say 'check' to Check your inbox")
    




    say= gTTS(text=" Select your choice  ", lang='en')
    ##convert=("3.mp3")
    ##say.save(convert)
    ##music = pyglet.media.load(convert, streaming = False)
    ##music.play()
    ##time.sleep(music.duration)
    ##os.remove(convert)
    # music.play()
    # time.sleep(music.duration)
    # os.remove(convert)
    speak("select your choice")


    speech5 = sr.Recognizer()
    with sr.Microphone() as source:
        speech5.adjust_for_ambient_noise(source,duration=1)
        print ("\tYour choice:\n")
        speech6=speech5.listen(source)
        print ("\t\t\tCommand Accepted\n")

    try:
        text=speech5.recognize_google(speech6)
        print ("\t\tYou said : "+text)
        speak("You said : "+text)
       
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again")
         
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))


    if text == 'compose' or text == 'compoze' or text == 'compus' or text== 'kompoz' or text =="impose":


    ##    say= gTTS(text="Enter receiver's id", lang='en')
    ##    convert=("4.mp3")
    ##    say.save(convert)
    ##    music = pyglet.media.load(convert, streaming = False)
    ##    music.play()
    ##    time.sleep(music.duration)
    ##    os.remove(convert)
        speak("Enter receiver's id")


        speech9 = sr.Recognizer()
        with sr.Microphone() as source:
            speech9.adjust_for_ambient_noise(source,duration=1)
            print (" \t\t enter recievers email   :\n")
            # speech10=speech9.listen(source)

            # speech11=((speech9.recognize_google(speech2)).replace(" ", "")).lower()
            # speech11=(().replace(" ", "")).lower()
            speech11=speech9.listen(source)

            print ("\t\t\tCommand Accepted\n")
        try:
            text2=((speech9.recognize_google(speech11)).replace(" ", "")).lower() + "@gmail.com"
            print ("\tYou said :"+text2)
            speak("You said :"+text2)
            rec_mail = text2
        except sr.UnknownValueError:
            print("Can't Understand the command. Run Again.")
        except sr.RequestError as e:
            print("Could not Connect to the Internet; {0}".format(e))

       

        speech7 = sr.Recognizer()
        with sr.Microphone() as source:
            speech7.adjust_for_ambient_noise(source,duration=1)

            print (" \t\tSay Your message  :\n")
            speak("say your message")
            speech8=speech7.listen(source)
            print ("\t\t\tCommand Accepted\n")
        try:
            text1=speech7.recognize_google(speech8)
            print ("\tYou said :"+text1)
            speak("You said :"+text1)
            msg = text1
        except sr.UnknownValueError:
            print("Can't Understand the command. Run Again.")
        except sr.RequestError as e:
            print("Could not Connect to the Internet; {0}".format(e))




        # mail = smtplib.SMTP('smtp.gmail.com',465)    
        # mail.ehlo()
        # mail.starttls()
        # # mail.login(email_id,password )
        # mail.login(email_id,'rxvcdgvrjfrjtigb' )
        # mail.sendmail(email_id,rec_mail,msg)

       

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email_id, "rxvcdgvrjfrjtigb")
        server.sendmail(
      email_id,
      rec_mail,
      msg)
        print("the code is working successfully")
        server.quit()
        print (" \t\tYour message Has been Sent. ")
    ##    say = gTTS(text="Your message Has been Sent", lang='en')
    ##    convert=("3.mp3")
    ##    say.save(convert)
    ##    music = pyglet.media.load(convert, streaming = False)
    ##    music.play()
    ##    time.sleep(music.duration)
    ##    os.remove(convert)
        speak("your message has been sent")
        # mail.close()  
    if text == 'check' or text == 'chuck' or text == 'jack' or text == 'chack'  :
       
        # account credentials
        username = "chandramahi68@gmail.com"
        password = "mahi@123"
        speak("now we will be reading your emails ")
        # use your email provider's IMAP server, you can look for your provider's IMAP server on Google
        # or check this page: https://www.systoolsgroup.com/imap/
        # for office 365, it's this:
        imap_server = "imap.gmail.com"

        def clean(text):
            # clean text for creating a folder
            return "".join(c if c.isalnum() else "_" for c in text)

        # create an IMAP4 class with SSL
        imap = imaplib.IMAP4_SSL(imap_server)
        # authenticate
        imap.login(username, password)


        status, messages = imap.select("INBOX")
        # number of top emails to fetch
        print("please enter the no of mails which you want to read from your inbox")
        speak("please enter the number  of mails which you want to read from your inbox")
        speech1 = sr.Recognizer()
        with sr.Microphone() as source:
            speech1.adjust_for_ambient_noise(source,duration=1)
            print ("\tno. of emails  :\n")
            speech2=speech1.listen(source)
            print ("\t\t\tCommand Accepted\n")

        try:
            n=((speech1.recognize_google(speech2)))
           
            print ("\t\tYou said :" ,n)
            speak("You said :" +n)
           
        except sr.UnknownValueError:
            print("Can't Understand the command. Run Again")
             
        except sr.RequestError as e:
            print("Could not Connect to the Internet; {0}".format(e))


        # total number of emails
        a=int
        messages = int(messages[0])
        for i in range(messages, messages-a, -1):
            # fetch the email message by ID
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode(encoding)
                        #print("Subject:", subject)
                       
                    speak("SUBJECT "+subject)

                       
                    print("Subject:", subject)
                    # decode email sender
                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                        #print("From:", From)
                    speak ("FROM "+ From )

                       
                    print("From:", From)
                    #print("Subject:", subject)
                    #print("From:", From)
                    print("="*100)

                   
        # close the connection and logout
        imap.close()
        imap.logout()









##    else:
##        print("please choose the apt command!")
##        speak("you said something wrong please run the program again ")
    speak("do you want to run again the program ,say yes  to run and no to exit ")
    speech5 = sr.Recognizer()
    with sr.Microphone() as source:
        speech5.adjust_for_ambient_noise(source,duration=1)
        print ("\tYour choice:\n")
        speech6=speech5.listen(source)
        print ("\t\t\tCommand Accepted\n")

    try:
        ans =speech5.recognize_google(speech6)
        print ("\t\tYou said : ",ans)
       
    except sr.UnknownValueError:
        print("Can't Understand the command. Run Again")
         
    except sr.RequestError as e:
        print("Could not Connect to the Internet; {0}".format(e))

speak("thank you for using our software .please do visit again")