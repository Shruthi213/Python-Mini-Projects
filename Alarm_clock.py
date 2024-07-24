from playsound import playsound
import time

CLEAR = "\33[2J"
CLEAR_AND_RETURN = "\33[H"


def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:2d}")


playsound("alarm.mp3")
minutes = int(input("How many minutes set: "))
seconds = int(input("How many seconds set: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
