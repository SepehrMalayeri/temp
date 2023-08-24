from playsound import playsound
from time import sleep, ctime

alert_file = "C:/Users/dpc/Desktop/Alert Files/situp - move alert.mp3"  # Path To ALert Sound File


def play_alarm(alert_sound):
    for i in range(6):
        playsound(alert_sound)

wait_time = 10 * 60  # Wait Time In Seconds

while True:
    sleep(wait_time)
    if ctime()[11:13] == "21":  # time for brushing
        for i in range(2):
            play_alarm(alert_file)
    else:
        play_alarm(alert_file)
    