# Recommending Songs on Spotify with Machine Learning

Insert image of Spotify playlist

Check out my in-depth analysis on Medium here: (insert link)
## Intro


## Installation
Clone this repo, create a blank Anaconda environment, and install the requirements file.
```bash
# Creates new environment called 'spotify_recommender'
conda create -n spotify_recommender python=3.9
# Activates the environment we just made
conda activate spotify_recommender-env
# Install the requirements
pip install -r requirements.txt
```
## Usage
### Spotify's API

To get your Spotify data, it is necessary to use Spotify's API. In order to do this, become a developer and create an app at this link:

https://developer.spotify.com/dashboard/

Go to your new developer dashboard and click on ‘Create an App’. You can name it whatever you want, just try to avoid using ‘Spotify’ in the name, or it might get blocked.

We need to provide a ‘redirect link’ that we’ll use to collect the user’s permission. From your app’s panel in the developer dashboard, click on ‘Edit Settings’ and add a link under Redirect URIs. This doesn’t have to be a real link: if you don’t have a website, you can simply use http://localhost:7777/callback.
You will also need your app’s Client ID and Client Secret. You’ll find them in the app panel under your app’s name. Now you have all you need to access the Spotify API!

## References
[Get Your Spotify Streaming History With Python](https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3#:~:text=Getting%20the%20data,option%20to%20request%20your%20data.)

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