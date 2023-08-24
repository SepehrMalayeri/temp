from playsound import playsound
from time import sleep
from datetime import now


alert_file = "C:/Users/dpc/Desktop/Alert Files/situp - move alert.mp3"  # Path To ALert Sound File


def play_alarm(alert_sound, repeats):
    """ Play the given file path 'repeats' times. """
    for i in range(repeats):
        playsound(alert_sound)


wait_time = 10 * 60  # Wait Time In Seconds

while True:
    sleep(wait_time)  # Wait for the next alarm
    hour = int(datetime.datetime.now().hour)  # Get the current hour
    
    # Check for specified hours
    if hour == 21:
        for i in range(2):  # Play the alert sound 12 times
            play_alarm(alert_file)
    else:
        play_alarm(alert_file)
    
    
    

