from instaloader import Instaloader, Profile

# Check a set list of instagram accounts/hashtags for new posts

# Each new posts check for "giveaway, free, win" , "by tonight", "by 12pm"

# See if post says to like, comment, or tag others
# Do that^

# notify me via email if won something (monitor notifications)

#https://www.promptcloud.com/blog/how-to-scrape-instagram-data-using-python
# https://instaloader.github.io/

#TODO find out how I want to get new posts

USERNAME = 'retreataggies'

# Creating .json files of each post
# See parameters here: https://instaloader.github.io/as-module.html#instaloader-main-class
L = Instaloader(download_pictures=False, download_videos=False, download_geotags=False, compress_json=False, download_comments=False, download_video_thumbnails=False, post_metadata_txt_pattern='')
profile = Profile.from_username(L.context, USERNAME)

for post in profile.get_posts():
    L.download_post(post, target=profile.username)


