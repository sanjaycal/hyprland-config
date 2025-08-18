import os
import subprocess

CURRENT_VOLUME = float((subprocess.run(["wpctl","get-volume","@DEFAULT_AUDIO_SINK@"], capture_output = True, text=True).stdout).split(":")[-1])

notifid = 1

if CURRENT_VOLUME>0:
    notifid = subprocess.run(["notify-send","-rp", str(notifid), f"🔊{CURRENT_VOLUME*100}%"], capture_output=True, text=True).stdout.strip()
else:
    notifid = subprocess.run(["notify-send","-rp", str(notifid), f"🔇{CURRENT_VOLUME*100}%"], capture_output=True, text=True).stdout.strip()


