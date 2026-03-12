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