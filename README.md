# Recommending Songs on Spotify with Machine Learning

![Sample Playlist Generated](.images/playlist_screenshot.jpg "Sample Playlist Generated")

Check out my in-depth description on Medium here: (insert link)
## Intro


## Installation & Requirements

Clone this repo, create a blank Anaconda environment, and install the requirements file.
```bash
# Creates new environment called 'spotify_recommender'
conda create -n spotify_recommender python=3.9
# Activates the environment we just made
conda activate spotify_recommender-env
# Install the requirements
pip install -r requirements.txt
```

To get your Spotify data, it is necessary to use Spotify's API. In order to do this, become a developer and create an app at this link:

https://developer.spotify.com/dashboard/

Go to your new developer dashboard and click on ‘Create an App’. You can name it whatever you want, just try to avoid using ‘Spotify’ in the name, or it might get blocked.

We need to provide a ‘redirect link’ that we’ll use to collect the user’s permission. From your app’s panel in the developer dashboard, click on ‘Edit Settings’ and add a link under Redirect URIs. This doesn’t have to be a real link: if you don’t have a website, you can simply use http://localhost:7777/callback.

Take note of your client ID and client secret. You’ll find them in the app panel under your app’s name. 

If you'd like to explore your streaming history, access your Spotify account dashboard at https://www.spotify.com/. In the privacy settings, you’ll find the option to request your data. This requires some patience. Spotify says it takes up to thirty days, but it’s usually much faster.

Once you've got your streaming history, clone [this GitHub repo ](https://github.com/vlad-ds/spoty-records)to create a dataframe of your streaming history. The dataframe created from that repo can replace the file 'streaming_history.csv' in this repo. 

Now you have all you need to access the Spotify API!
## Usage

### Data Exploration


## References
[Get Your Spotify Streaming History With Python](https://github.com/vlad-ds/spoty-records)

[Airflow for Beginners - Run Spotify ETL Job in 15 minutes!](https://www.youtube.com/watch?v=i25ttd32-eo&t=14s)

[Spotipy Documentation](https://spotipy.readthedocs.io/en/2.7.0/)
## Contact
Feel free to reach out to me on LinkedIn and follow my work on Github! 

<br>
<p align="center">
<a href="https://www.linkedin.com/in/logannorman/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="https://github.com/lognorman20">
<img src="https://img.shields.io/badge/github-%23100000.svg?&style=for-the-badge&logo=github&logoColor=white"/>
</a>
</p>