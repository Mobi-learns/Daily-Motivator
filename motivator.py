# import requests

# url = "https://quotes.rest/qod?language=en"
# res = requests.get(url=url)
# print(res)


# import requests

# url = "https://quotes.rest/qod?language=en"
# api_key = "MYo8wR94Tv984GKofWwyD3HpNBBSUXfVSpc31fjp"  # Replace this with your actual API key

# # Including the API key in the headers
# headers = {"X-TheySaidSo-Api-Secret": api_key}
# res = requests.get(url=url, headers=headers)

# # #print(res)
# data = res.json()
# print(data['contents']['quotes'][0]['quote'])
# # data_dict = {'success': {'total': 1},
# #             'contents': {'quotes': [{'id': '7THrdz0EivKNrF_FYxpYYweF', 'quote': 'People who are crazy enough to think they can change the world, are the ones who do.', 'length': 84, 'author': 'Apple Computers', 'language': 'en', 'tags': ['inspire', 'change-the-world'], 'sfw': 'sfw', 'permalink': 'https://theysaidso.com/quote/apple-computers-people-who-are-crazy-enough-to-think-they-can-change-the-world-a', 'title': 'Inspiring Quote of the day', 'category': 'inspire', 'background': 'https://theysaidso.com/assets/images/qod/qod-inspire.jpg', 'date': '2023-12-18'}]}, 'copyright': {'url': 'https://quotes.rest', 'year': '2023'}}
# # print(data_dict['contents']['quotes'][0]['quote'])









import requests
from twilio_conn import send_whatsapp_text, set_twilio_connection

account_sid= "ACb9e3680df52036c7847bcbf86f4d5422"
auth_token= "7c8f75b0d329d50d7d2b0d18f6d7fd03"

# Set up the Twilio client
client = set_twilio_connection(account_sid, auth_token)

def get_random_quote():
    url = "https://api.quotable.io/random"
    res = requests.get(url=url)
    data_dict = res.json()
    message = f'"{data_dict["content"]}"\n- {data_dict["author"]}'
    return message

quote = get_random_quote()
print(f'"{quote}"')

send_whatsapp_text(client, quote)

#  Set up the Twilio client
# client = set_twilio_connection(account_sid, auth_token)
# url = "https://api.quotable.io/random"
# res = requests.get(url=url)
# data_dict = res.json()
# # print('"' + data['content']+ '"')
# print(f'"{data_dict["content"]}"\n- {data_dict["author"]}')


# send_whatsapp_text(client,data_dict['content'])


#data_dict = {'_id': '_cllvgW3qw9C', 
            #  'content': 'Most powerful is he who has himself in his own power.', 'author': 'Seneca the Younger', 'tags': ['Famous Quotes'], 'authorSlug': 'seneca-the-younger', 'length': 53, 'dateAdded': '2020-12-19', 'dateModified': '2023-04-14'}
# Print the quote and author name
# print('"' + quote["content"] + '"')
# print('- ' + quote["author"])
# print(data_dict['content'])

