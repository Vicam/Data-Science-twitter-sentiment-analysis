import oauth2 as oauth
import urllib2 as urllib
import json

# See assignment1.html instructions or README for how to get these credentials

api_key = "0sAdStVrkzUxiayo8KP2BAKTi"
api_secret = "UThjbQ3Ky4rtrTTLMcnDx4xgKSqwHuFDfQiGYhbUzS9Mb3JXkI"
access_token_key = "747168278976544768-RniKN89lA8Vrsa0vFELQnLKIixgklft"
access_token_secret = "FIWZAFjopKHcz3SWHc5qc0ydxqPL2AbXrFNgLlwPNhBr2"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://api.twitter.com/1.1/search/tweets.json?q=microsoft"
  #  url = "https://stream.twitter.com/1.1/statuses/sample.json" #
  # https://api.twitter.com/1.1/search/tweets.json?q=microsoft #
  parameters = []
  response = twitterreq(url, "GET", parameters)
  """for line in response:
    print line.strip()"""
  result1 = json.load(response)
  result2 = result1["statuses"]
  print result1.keys()[1]
  print result1[result1.keys()[1]]
  """result2Keys = ["contributors", "truncated", "text", "is_quote_status", "in_reply_to_status_id", "id", 
  "favorite_count", "entities", "retweeted", "coordinates", "source", "in_reply_to_screen_name", "in_reply_to_user_id", 
  "retweet_count", "id_str", "favorited", "user", "geo", "in_reply_to_user_id_str", 
  "possibly_sensitive", "lang", "created_at", "in_reply_to_status_id_str", "place", "metadata" ]
  for keys in result2Keys:
	print keys, result2[0][keys]"""
  

if __name__ == '__main__':
  fetchsamples()
