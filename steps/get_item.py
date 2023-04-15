import openai
import sys
sys.path.append('../')
import config
import json

def get_item(msg):
        
    ret_item = False
        
    openai.api_key = config.openai_api_key

    prompt = f"Message: {msg}.\n For the message above, extract the physical items and put them into a json object, with the item name as the key, and item quantity as the value."

    ret_item = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=40,
        temperature=0.1
    )

    if ret_item:
        ret_item =  ret_item['choices'][0]['text']
        ret_item = json.loads(ret_item)

    return ret_item


# print(type(get_item('can I have 1 banana and two potatoes')))
# print(get_item('can I have 1 banana and two potatoes'))
# print(get_item('can I have a cheese cake please?'))