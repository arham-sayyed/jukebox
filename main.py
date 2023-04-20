from download_audio import download_audio
from audio_merger import merge_audios
from imageHub.getImage import get_image
from videocreator import create_video



def main():
    links = input("links: ")
    title = input("name of output file: ")
    query = input("Describe image in few words: ")

    download_audio(links) # --> None (only downloads audios)
    image = get_image(query= query) # --> image path 

    final_audio = merge_audios(title= title)[0] # --> final audio path
        
    if final_audio is None: # check if final audio is ready
        print("there's an error")
        exit()

    create_video(image_file= image, audio_file= final_audio , title= title)

        
if __name__ == "__main__":
    main()



