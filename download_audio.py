import os
from pytube import YouTube

def download_audio(input_links):
    links = listify(input_links)
    for link in links:
        try:
            audio = YouTube(link)
            title = purify(audio.title)
            
            output_path = os.path.join(os.getcwd(), "audios")
            audio_stream = audio.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=output_path, filename=f"{title}.mp3")
            print(f"{title} is downloaded")
        except Exception as e:
            print(f"Error while processing link: {link}. Error message: {e}")

def listify(text):
    if isinstance(text, str):
        links = list(filter(None, text.strip().split(" ")))
        return links
    elif isinstance(text, list):
        return text
    else:
        raise ValueError("Input must be a string or a list")


def purify(sentence):
    filtered_sentence = ""
    chars = [" ", "." , "<" , ">" , ":" , '"' , "/" , "\\" ,"|" , "?" , "*" , "%" , "#" , "@" , "!" , "}" , "{" , "+" , "-" , "=" , ")" , "(" , "&" , "$" , "_" , "'" , "`" , "~" , ";" , "," , "[" , "]" ]
    for char in sentence:
        if char not in chars:
            filtered_sentence += char
    return filtered_sentence