import time
import sys
from win10toast import ToastNotifier

notifier = ToastNotifier()

WORK_TIME = 25 * 60
PAUSE_TIME = 5 * 60

NOTIF_TITLE = "Pomodoro"
NOTIF_WORK_TEXT = "Lavoro"
NOTIF_PAUSE_TEXT = "Pausa"
NOTIF_END_TEXT = "Fine"

HOUR_UNITY_SAMPLES = {"h", "o", "ora", "ore"}
MIN_UNITY_SAMPLES = {"m", "min", "mins", "minuto", "minuti"}

quantity = sys.argv[1]
unity = sys.argv[2]


def define_seconds(q, u):
    
    if(u.lower() in HOUR_UNITY_SAMPLES):
        return q * 3600

    elif(u.lower() in MIN_UNITY_SAMPLES):
        return q * 60


def start_session(s):
    
    while s:
        if(s >= WORK_TIME):
            start_timer(WORK_TIME, True)
            s -= WORK_TIME

        if(s >= PAUSE_TIME):
            start_timer(PAUSE_TIME, False)
            s -= PAUSE_TIME

    stop_session()


def start_timer(s, isWork):
    
    go_off(isWork)

    while s:
        time.sleep(1)
        s -= 1
        print(s)


def go_off(isWork):

    if(isWork):
        notification_text = NOTIF_WORK_TEXT
    else:
        notification_text = NOTIF_PAUSE_TEXT
    
    notifier.show_toast(NOTIF_TITLE, notification_text)


def stop_session():

    notifier.show_toast(NOTIF_TITLE, NOTIF_END_TEXT)


#main
start_session(define_seconds(int(quantity), unity))