from moviepy.editor import AudioFileClip, concatenate_audioclips
import glob , os

def audio_paths(): # ---> not called in main.py
    
    audio_paths = glob.glob("audios/*.mp3") # glob to collect all the audios paths need --> list
    return audio_paths



def load_audios(): # --->  no calling in main.py
    audios = [] # empty list to hold the paths in future

    for path in audio_paths(): # audio_paths() --> list
        audio = AudioFileClip(path) # creating audio objects of moviepy for all the audios
        audios.append(audio) # appending in the audios list
    
    return audios # --> list 



def merge_audios(title):
    print("merging audios")
    try:
        final_audio = concatenate_audioclips(clips= load_audios())
        final_audio.write_audiofile(f"final_audio/{title}.mp3")
        print("audios merged successfully!")
        final_audio_path = f"final_audio/{title}.mp3"
        
        files = audio_paths()

        for file in files:
            os.remove(file)

        return [final_audio_path , True]
        
    except Exception as e:

        print(f"ERROR while 'merge_audios': {e}")
        return [None, None]