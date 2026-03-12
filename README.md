# Python-WhatsApp-Message-Sender-Without-PyWhatKit-

Python WhatsApp Message Sender (Without PyWhatKit)

A simple Python automation script that sends WhatsApp messages automatically without using the PyWhatKit library.
The script uses Python's webbrowser module to open the WhatsApp API link and pyautogui to automate keyboard actions for sending the message.

This project demonstrates basic Python automation and interaction with WhatsApp Web.

Features

Send WhatsApp messages automatically

Works without PyWhatKit

Supports multiple phone numbers

Automatically adds +91 country code if missing

Uses keyboard automation to send messages

Automatically closes the WhatsApp tab after sending

Technologies Used

Python

webbrowser module

pyautogui

time

Project Workflow

A list of phone numbers is stored in the script.

The program checks whether the number contains the +91 country code.

If not, the code automatically adds +91.

The script opens the WhatsApp chat using the API URL.

The message is automatically filled in the chat.

pyautogui presses Enter to send the message.

The browser tab is closed automatically.

Code Example
import webbrowser
import time
import pyautogui

p_no=["7796080589","+919422544204"]

def wpmsg():
    msg="hii"
    url=f"https://api.whatsapp.com/send?phone={c}&text={msg}"
    webbrowser.open(url)
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('alt','f4')
    time.sleep(2)
    pyautogui.hotkey('alt','f4')

for c in p_no:
    if not c.startswith("+91"):
        c="+91"+c
        wpmsg()
    else:    
        wpmsg()
Requirements

Install the required Python library before running the script.

pip install pyautogui
How to Run

Clone the repository

git clone https://github.com/Purvap08/Python-WhatsApp-Message-Sender-Without-PyWhatKit-.git

Navigate to the project folder

cd Python-WhatsApp-Message-Sender-Without-PyWhatKit-

Run the Python script

python main.py
Important Notes

Make sure you are logged in to WhatsApp Web in your browser.

Do not move the mouse or keyboard while the automation is running.

Internet connection is required.

Disclaimer

This project is created for educational and learning purposes only. Please use automation responsibly and respect WhatsApp policies.
