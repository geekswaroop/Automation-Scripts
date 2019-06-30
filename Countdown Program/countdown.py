import time, subprocess

timeleft=60
while timeleft > 0:
    print(timeleft, end="")
    time.sleep(1)
    timeleft-=1

subprocess.Popen(['start','alarm.wav'], shell=True)