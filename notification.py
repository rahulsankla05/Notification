import time
from plyer import notification
if __name__== "__main__":
    while True:

        # notification.notify(
        #     title ="Health Notification",
        #     message = "Take Medicine and drink water to keep hydrated",
        #     # app_icon = "D:\rs\python_harry\ Notification \icon.ico",
        #     timeout = 10
        # )
        # time.sleep(60*1)

        notification.notify(
            title = "Kratin Healthcare",
            message = "Hope you're feeling Awesome!!,Take your Medicine and drink water",
            # icon = "D:\rs\python_harry\Notification\hydrated.ico",
            timeout = 10       # notification will remain on screen till 10 sec//
        )
        time.sleep(60*0.5)         # Notification again will pop-up after 30 secs//

