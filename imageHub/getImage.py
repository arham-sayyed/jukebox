import requests , json , os
from imageHub.api_secrets import pexel_api_key



def image_downloader(json_obj):
    if json_obj is not None:
        url = json_obj['photos'][0]['src']['landscape']
        filename = f"images/{purify(json_obj['photos'][0]['alt'])}.png"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            return filename
    return None




def description_genrator(json_obj):
    
    if json_obj is not None:

        image_source = json_obj['photos'][0]['url']

        photographer = json_obj['photos'][0]['photographer']

        photographer_url = json_obj['photos'][0]['photographer_url']

        image_credits = f"Background Image Source: {image_source} \nPhotographer: {photographer} \nYou can find the photographer @ {photographer_url}"
        
        return image_credits



def purify(sentence):
    filtered_sentence = ""
    chars = [" ", "." , "<" , ">" , ":" , '"' , "/" , "\\" ,"|" , "?" , "*" , "%" , "#" , "@" , "!" , "}" , "{" , "+" , "-" , "=" , ")" , "(" , "&" , "$" , "_" , "'" , "`" , "~" , ";" , "," , "[" , "]" ]
    for char in sentence:
        if char not in chars:
            filtered_sentence += char
    return filtered_sentence



def get_image(query):
    headers = {
        "Authorization" : pexel_api_key
    }
    params = {
        "query" : query,
        "per_page" : 1,
        "orientation": "landscape",
        # "color" : "violet" | possibles --> red , orange, yellow, green, turquoise, blue, violet, pink, brown, black, gray, white  or hexadecimals like #ffffff
        "size": "large"
    }

    url = "https://api.pexels.com/v1/search"
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        response_dict = response.json()
        # print(response_dict)
        
        filename = image_downloader(json_obj=response_dict)
        image_credits = description_genrator(json_obj=response_dict)
        
        return filename

        # return {"filename": filename, "credits": image_credits}
    
    else:
        return None

    


# image = get_image("plain long empty road aesthetic")

# print(image)



# filename = image['filename']
# credits = image['credits']

# print(filename)
# print(credits)

