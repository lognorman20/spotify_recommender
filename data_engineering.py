def auth():
    # Insert your Spotify username and the credentials that you obtained from spotify developer
    username = "yvngflash_"
    cid = "58ecd7aadf294b9aa038a3080ef670cb"
    secret = "4a277ac2c0a744eea5c839b1ecb27002"
    redirect_uri = "http://localhost:7777/callback"
    scope = "user-top-read playlist-modify-private playlist-modify-public"

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=cid,
            client_secret=secret,
            redirect_uri=redirect_uri,
            scope=scope,
            username=username,
        )
    )


import time
import os
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import random
from functools import reduce
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

auth()
# Once the Authorisation is complete, we just need to `sp` to call the APIs

# token = util.prompt_for_user_token(
#     username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect_uri
# )

# sp = spotipy.Spotify(auth=token)
