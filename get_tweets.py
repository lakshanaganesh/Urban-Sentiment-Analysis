import tweepy
import csv

#personal details from Twitter API
CONSUMERKEY = 
CONSUMERSECRET = 
ACCESSTOKENKEY = 
ACCESSTOKENSECRET = 

#Pass our consumer key and consumer secret to Tweepy's user authentication handler
auth = tweepy.OAuthHandler(CONSUMERKEY, CONSUMERSECRET)

#Pass our access token and access secret to Tweepy's user authentication handler
auth.set_access_token(ACCESSTOKENKEY, ACCESSTOKENSECRET)


api = tweepy.API(auth,wait_on_rate_limit=True)

#Error handling
if (not api):
    print ("Problem connecting to API")

# Passing a query to find tweets specific to New York
places = api.geo_search(query="New York")

place_id = places[0].id
searchQuery = 'place:'+ place_id
tweetCount = 0
#Printing csv file
with open('tweets.csv', 'a') as f:
    writer = csv.writer(f)
    for tweet in tweepy.Cursor(api.search,q= searchQuery).items() :         
        if tweet.place is not None:
            text = str(tweet._json['text'].encode("utf-8"))
            time = tweet._json['created_at']
            userid = tweet._json['user']['id']
            place = tweet._json['place']['full_name']
            print(text)
            writer.writerow([text, time, userid, place])
            tweetCount += 1

print(tweetCount)


