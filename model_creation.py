import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from imblearn.over_sampling import SMOTE

import sklearn
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.metrics import f1_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Importing playlist dataframes
df = pd.read_csv("data/encoded_playlist_songs.csv")
df_fav = pd.read_csv("data/favorite_songs.csv")

df = pd.concat([df, df_fav], axis=0)

# Shuffle dataset
shuffle_df = df.sample(frac=1)

# Define a size for your train set
train_size = int(0.8 * len(df))

# Split dataset
train_set = shuffle_df[:train_size]
test_set = shuffle_df[train_size:]

X = train_set.drop(columns=["favorite", "track_id"])
y = train_set.favorite

# Train / Split Data
oversample = SMOTE()
X_train, y_train = oversample.fit_resample(X, y)

X_test = test_set.drop(columns=["favorite", "track_id"])
y_test = test_set["favorite"]

# Testing models

# Logistic Regression
lr = LogisticRegression(solver="lbfgs", max_iter=400)
lr_scores = cross_val_score(lr, X_train, y_train, cv=10, scoring="f1")
print("Logistic Regression Baseline Score:")
print(np.mean(lr_scores))

# Hyperparameter tuning for decision tree classifier
parameters = {
    "max_depth": [3, 4, 5, 6, 10, 15, 20, 30],
}
dtc = Pipeline([("CV", GridSearchCV(DecisionTreeClassifier(), parameters, cv=5))])
dtc.fit(X_train, y_train)
print("Decision Tree Parameters:")
print(dtc.named_steps["CV"].best_params_)

# Decision Tree Classifier
dt = DecisionTreeClassifier(max_depth=30)
dt_scores = cross_val_score(dt, X_train, y_train, cv=10, scoring="f1")
print("Decision Tree Classifier Score:")
print(np.mean(dt_scores))

# Hyperparameter optimization of RandomForestClassifier
parameters = {"max_depth": [3, 6, 12, 15, 20], "n_estimators": [10, 20, 30]}
clf = Pipeline([("CV", GridSearchCV(RandomForestClassifier(), parameters, cv=5))])
clf.fit(X_train, y_train)
print("RandomForestClassifier Parameters:")
clf.named_steps["CV"].best_params_

# RandomForestClassifier
rf = Pipeline([("rf", RandomForestClassifier(n_estimators=10, max_depth=20))])
rf_scores = cross_val_score(rf, X_train, y_train, cv=10, scoring="f1")
print("Decision Tree Classifier Score:")
np.mean(rf_scores)

# Using algorithm on test data

# Building a pipeline to use on regular data
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

pipe = make_pipeline(
    StandardScaler(), RandomForestClassifier(n_estimators=30, max_depth=20)
)
pipe.fit(X_train, y_train)  # apply scaling on training data
Pipeline(
    steps=[
        ("standardscaler", StandardScaler()),
        ("rf", RandomForestClassifier(n_estimators=30, max_depth=20)),
    ]
)
pipe.score(X_test, y_test)

# Predicting songs and saving to dataset

df = pd.read_csv("data/encoded_playlist_songs.csv")  # resetting df

prediction = pipe.predict(df.drop(["favorite", "track_id"], axis=1))
df["prediction"] = prediction

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import oauth2

# Insert your Spotify username and the credentials that you obtained from spotify developer
cid = "58ecd7aadf294b9aa038a3080ef670cb"
secret = "4a277ac2c0a744eea5c839b1ecb27002"
redirect_uri = "http://localhost:7777/callback"
username = "yvngflash_"

# Once the Authorisation is complete, we just need to `sp` to call the APIs
scope = "user-top-read playlist-modify-private playlist-modify-public"
token = util.prompt_for_user_token(
    username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect_uri
)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)


def create_playlist(sp, username, playlist_name, playlist_description):
    playlists = sp.user_playlist_create(
        username, playlist_name, description=playlist_description
    )


create_playlist(
    sp, username, "Your New Jams", "This playlist was created using python!"
)


def fetch_playlists(sp, username):
    """
    Returns the user's playlists.
    """

    id = []
    name = []
    num_tracks = []

    # Make the API request
    playlists = sp.user_playlists(username)
    for playlist in playlists["items"]:
        id.append(playlist["id"])
        name.append(playlist["name"])
        num_tracks.append(playlist["tracks"]["total"])

    # Create the final df
    df_playlists = pd.DataFrame({"id": id, "name": name, "#tracks": num_tracks})
    return df_playlists


playlist_id = fetch_playlists(sp, username)["id"][0]


def enrich_playlist(sp, username, playlist_id, playlist_tracks):
    index = 0
    results = []

    while index < len(playlist_tracks):
        results += sp.user_playlist_add_tracks(
            username, playlist_id, tracks=playlist_tracks[index : index + 50]
        )
        index += 50


list_track = df.loc[df["prediction"] == 1]["track_id"]
enrich_playlist(sp, username, playlist_id, list_track)
