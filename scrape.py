import snscrape.modules.twitter as twitterScraper
import json
import time


#scraper = twitterScraper.TwitterUserScraper("KermitTheFrog")
scraper = twitterScraper.TwitterListPostsScraper("Elon Musk")

tweets = []

# function tweet_to_tweet has a list of properties of tweet objects
start = time.time()
for index, tweet in enumerate(scraper.get_items()):
    if index > 500:
        break
    tweets.append({"id": tweet.id, "content": tweet.rawContent,
                  "likes": tweet.likeCount, "replies": tweet.replyCount, "retweets": tweet.retweetCount})

end = time.time()
print("time elapsed: ", end - start)

f = open("tweets.json", "w")
j = json.dumps(tweets)
f.write(j)
