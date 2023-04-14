import tweepy
import random
import openai
import requests
import json


#Creates a list of the top headlines from newsapi and selects a random headline
def headlines():
    headline_list = []
    news = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY')
    content = news.json()
    articles = content['articles']
    for article in articles:
        title = article['title']
        first_field = title.split('-')[0].strip()
        headline_list.append(first_field)
    return(random.choice(headline_list))

#generates an original tweet about the headline
def airesult():
    openapi_api_key = #openaiapikey
    prompt: f"In your own words, write a tweet about the following subject: {headlines()}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
    )

    result = response.choices[0].text
    return result


#posts the tweet 
def tweet():
    auth = tweepy.OAuthHandler(
    #twitter id, twitter secret
)
    auth.set_access_token(
    #twitter acccess tokens,
)
    api = tweepy.API(auth)

    api.update_status(airesult())

if __name__ == "__main__":
   tweet()