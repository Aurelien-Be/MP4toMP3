import os
from moviepy.editor import *
clip = AudioFileClip(os.path.join(R"C:\Users\Asus\Downloads", "mon_enregistrement_3.m4a"))
clip.write_audiofile(os.path.join(R"C:\Users\Asus\Downloads", "fleursdumal.mp3"))
