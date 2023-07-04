# Notification
Desktop Notification 
1) Here I used the Time and Plyer inbuilt library function of Python.
2) With the help of notification.notify() method I successfully created a Desktop Notification system, with few lines of Code.
3) Timeout defines how long the Notification will remain on screen.
4) time.sleep(): it defines that after this time we'll get a notification again.

Python Code:
# code#
import time
from plyer import notification
if __name__== "__main__":
    while True:
        notification.notify(
            title = "Kratin Healthcare",         # Title of the Notification
            message = "Hope you're feeling Awesome!!,Take your Medicine and drink water",          # Main message 
            # icon = "D:\rs\python_harry\Notification\hydrated.ico",      # for icon on notification message
            timeout = 10       # notification will remain on screen till 10 sec//
        )
        time.sleep(60*0.5)         # Notification again will pop-up after 30 secs//

5)** Screenshot of Notification**
https://docs.google.com/document/d/1exkUDVOHnljo2WrTPvSO3RPMy70jeBl0TxHWlsOYAEc/edit?usp=sharing


