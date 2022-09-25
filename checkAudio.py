from subprocess import check_output
import subprocess

# import subprocess
import json
import os





def has_audio_streams(file_path):
    command = ["ffmpeg", "-i", file_path, "-af",  "ebur128=framelog=verbose",  "-f", "null", "-"]

    output = check_output(command, stderr=subprocess.STDOUT);

    return float(str(output).split("I:         ")[1].split(" ")[0])

print(os.listdir())

for f in os.listdir():
    if f.split(".")[-1] == "ts":
        print(f, ": ",)
        print(has_audio_streams(f))
