#!/usr/bin/env python3


import sys
from twython import Twython

sys.path.insert(0, 'credentials/') ##add the credentials folder
import credentials

## Credential appraisal - hail to the lord
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_KEY = credentials.ACCESS_KEY
ACCESS_SECRET = credentials.ACCESS_SECRET

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
# print(twitter.verify_credentials()) ##debug

from markov import manfred_sagt

twitter.update_status(status=manfred_sagt())
