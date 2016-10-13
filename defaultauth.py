#NOTE Copy this file to auth.py then add your keys to auth.py To turn the code on!
# In terminal rul following:
# 1) cp defaultauth.py auth.py
# 2) open auth.py (Add and save twitter key, secret, token, token_secret)


class TwitterAuth:
	# Go to http://dev.twitter.com and create an app. 
	# The consumer key and secret will be generated for you after
    consumer_key="<YOURKEYGOESHERE>"
    consumer_secret="<YOURSECRET>"

	# After the step above, you will be redirected to your app's page.
	# Create an access token under the the "Your access token" section
    access_token="<YOURTOKEN>"
    access_token_secret="<TOKENSECRET>"
