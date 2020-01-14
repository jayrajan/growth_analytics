# Code written by Jerin Rajan by 03rd Jan 2019
# Email - jrajan@jprtech.co.uk

# PLEASE NOTE:
# Read requirements.txt document before running this script.

import pandas as pd
import json
from datetime import datetime, timezone
import time
import tweepy
from urllib.request import urlopen
import urllib.error
import re
import os
from fuse_image import fuse_logo

# # TWITTER KEY & TOKEN - @api_hour
CONSUMER_KEY = 'oBiIhg7ZF5wefAihCCm1rl1Wj'
CONSUMER_SECRET = 'bG6DjIFrIaqsrIFv5pafCXRbGtpC6nYz8HIcMJxocHQ6sQGkes'
ACCESS_TOKEN = '290090813-XSgGWVmRde2FT3o4DgBoRMkyxqSqHCXUMD5in5Vt'
ACCESS_TOKEN_SECRET = 'sPUVX7l1sXgUkxf25nw1PCdS55Os3caTmOA3IE6RPOI7s'

# INITIALISATION
tweet_txt = list()
tweet_id = list()
# Time scheduler in seconds
post_time = 5

# EXCEL - RAW FILE - Read the Excel file data
fname = input('Enter Filename: ')
xl_data = pd.read_excel(fname, sheet_name='data_table')

# JSON - CONVERSION
xl_json = xl_data.to_json(orient='records')
js = json.loads(xl_json)

# TWITTER CONNECTION
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create Twitter API object
api = tweepy.API(auth)

# Create a new folder-images in current directory to save the url images
path = './fusion'
try:
    os.mkdir(path)
    print('created driectory')
except OSError:
    print('FAILED')

# PARSING THE JSON
for item in js:
    tweet_id = item['post_id']
    tweet_txt = item['post_text'][:250]
    # Time & Date in EPOCH
    tweet_date = item['post_datetime']
    # Converting from EPOCH time and date to UTC time and Date
    tweet_dt_utc = str(datetime.fromtimestamp(int(str(tweet_date)[:10])))
    # tweet_date = tweet_dt_utc[:10]
    # tweet_time = tweet_dt_utc[10:]
    tweet_img_url = item['post_img']

    try:
        # POSTING TWEET STATUS ONLY FOR NON IMAGE TWEETS
        if tweet_img_url is None:
            api.update_status(tweet_txt)
            print('\n Tweet:',tweet_id,'posted')
            time.sleep(post_time)
            continue
        else:
        # POSTING TWEET STATUS AND MEDIA IMAGES FROM URL WITH LOGO
            # clearning the URLs using regular expression
            img_url = re.findall('http[s]?://.+?.jpg|http[s]?://.+?.jpeg', tweet_img_url)

            # Extracting the URL string from the list
            url = img_url[0]

            # Fusing the logo with the URL Image
            new_image = fuse_logo(url,tweet_id)

            # Posting the Images and Status Text on Twitter
            status = api.update_with_media(new_image,tweet_txt)
            print('\n Tweet:',tweet_id,'posted')
            # Scheduling the post every 5 seconds
            time.sleep(post_time)
    except:
        continue
print('\n End of Tweet')
