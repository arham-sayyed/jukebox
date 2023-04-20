"""
It takes input as an image and writes the audio on that image and outputs the video as .mp4 
nothing too complicated  
"""
from moviepy.editor import *


def create_video(image_file, audio_file, title):
    try:

        output_file = f"final_videos/{title}.mp4"

        img_clip = ImageClip(image_file)
        audio_clip = AudioFileClip(audio_file)

        img_clip = img_clip.set_duration(audio_clip.duration)

        img_clip = img_clip.set_audio(audio_clip)

        img_clip.write_videofile(output_file, fps=24, codec='libx264' , bitrate="5000k")

    except Exception as e:
        print(f"ERROR while create_video: {e}")


# create_video("images/GrayscalePhotoofRoad.png" , "proto/didi.mp3","thirdtest-encodingrechange")