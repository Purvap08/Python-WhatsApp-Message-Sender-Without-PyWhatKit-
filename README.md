# Python-WhatsApp-Message-Sender-Without-PyWhatKit-

This project is a simple Python automation script that sends WhatsApp messages automatically without using the PyWhatKit library. The script uses the webbrowser module to open the WhatsApp API link and pyautogui to automate keyboard actions for sending the message.

The program takes a list of phone numbers, ensures they include the correct country code (+91), opens WhatsApp Web for each number, sends the message, and then closes the browser tab automatically.

This project demonstrates basic Python automation techniques and interaction with web applications.

Features

Send WhatsApp messages automatically

Works without using PyWhatKit

Supports multiple phone numbers

Automatically adds +91 country code if missing

Uses keyboard automation to send messages

Technologies Used

Python

webbrowser module

pyautogui for keyboard automation

WhatsApp API link (api.whatsapp.com)

How It Works

A list of phone numbers is provided in the script.

The script checks if the number contains the +91 country code.

It opens the WhatsApp chat using the API URL.

The message is pre-filled automatically.

pyautogui presses Enter to send the message.

The browser tab is closed automatically.
