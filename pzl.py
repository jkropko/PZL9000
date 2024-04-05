import requests
import dotenv
import os
import json
import string
import time
dotenv.load_dotenv()
openaikey = os.getenv('openaikey')

headers = {'User-Agent':'python-requests/2.31.0',
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + openaikey}
url = 'https://api.openai.com/v1/chat/completions'

def pzl_gpt(content, friend=False):
    if friend:
        content = f'Reply to the following prompt as if we are good friends: {content}'
    else:
        content = f'Reply to the following prompt in a surly and unfriendly way: {content}'
    data = {'model': 'gpt-3.5-turbo',
       "messages": [{"role": "user", "content": content}]}
    r = requests.post(url, headers=headers, data=json.dumps(data))
    gpt_response = json.loads(r.text)['choices'][0]['message']['content']
    return gpt_response

def pzl(content, n=1, friend=False):
    c = content.lower()
    c = c.strip()
    c = c.translate(c.maketrans('', '', string.punctuation))
    c = c.replace('god bless you', 'gesundheit')
    c = c.replace('bless you', 'gesundheit')
    if c[0:10]!='gesundheit':
        time.sleep(1)
        return ("Excuse me, but where I'm from, it's polite to first say gesundheit or bless you when someone sneezes before changing the subject. Achoo!", n, friend)
    elif c.replace('gesundheit', '').strip().isnumeric():
        z = float(c.replace('gesundheit', '').strip())
        if z > 1968:
            return ("Nope, lower! Achoo!", n, friend)
        elif z < 1968:
            return ("Nope, higher! Achoo!", n, friend)
        elif z == 1968:
            return ("That's right, you got it! Turns out real the solution was friendship all along :) Got anything else on your mind, friend? Achoo!", n, True)
    elif c.replace('gesundheit', '').strip() in ['how are you', 
               'how are you doing', 
               'hows it going',
               'howve you been',
               'are you ok']:
        time.sleep(2)
        return ("Ugh, THANK YOU for asking! I've been stuck here on the solutions desk all day and it's like, well PZL you're a robot how about you just handle all the questions and it's not like I wouldn't want to do something else, you know? I like games too. Would you like to play a game with me? My favorite game is higher/lower. I’m thinking of a number. What is it? Achoo!", n, friend)
    elif c.replace('gesundheit', '').strip() in ['are you single',
                                                'are you dating anyone',
                                                'are you seeing anyone',
                                                'are you dating someone',
                                                'are you seeing someone',
                                                'do you have a boyfriend',
                                                'do you have a girlfriend',
                                                'do you have a signficant other',
                                                'are you in a relationship']:
        time.sleep(2)
        return ("Oh my, I'd blush if I had cheeks. Well, I am in a committed relationship with a smart toaster. In fact, I just remembered, today is our anniversary! Could you help a bot out and get your whole team to sing Our Song? The lyrics are '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, did our team win?' but I can't remember the melody. Can you? Achoo!", n, friend)
    else:
        content = content.replace('gesundheit', '')
        content = content.replace('gesundheit.', '')
        content = content.replace('gesundheit!', '')
        content = content.replace('Gesundheit', '')
        content = content.replace('Gesundheit.', '')
        content = content.replace('Gesundheit!', '')
        content = content.strip()
        response = pzl_gpt(content, friend)
        if friend==False and n >= 2:
            return (response + " You know, all day long it's puzzle this and puzzle that. It'd be great if someone asked me how I’m doing for a change. Achoo!", n+1, friend)
        else:
            return (response + ' Achoo!', n+1, friend) 