import json
from instabot_py import InstaBot
from instaloader import Instaloader, Post
from instapy import InstaPy
from instagram.client import InstagramAPI
from instapy.util import smart_run
from secret import Secret

# I input the post and it goes and does the actions
# login credentials
user_login = Secret.user_login
user_password = Secret.user_password

#other function: make sure post is in english,
#other function: watch certain accounts for giveaways (retreat..)

########### just need to add in commenting and
# TODO add in "repost" function

# Logs in the instagram bot
bot = InstaBot(user_login, user_password)

def check_for_actions(post):
    caption = post['caption'].lower()

    if 'follow' in caption:
        # If it sees follow, follow the poster's profile
        # TODO add in possibly following others
        print('Follow found.')
        profile = post['username']
        follow_profile(post)

    if 'like' or 'double tap' or 'double-tap' in caption:
        # Likes the post
        print('Like found.')
        post_to_like = post['post_link']
        like_picture(post)

    if 'comment' in caption:
        # Comments on the post
        # TODO add in finding what to comment
        print('Comment found.')
        post_to_comment = post['post_link']
        #comment = ''
        #comment_on_post(post, comment)

    if 'tag' in caption:
        # Tags friends
        print('Tag found.')
        post_to_tag_on = post['post_link']
        comment = '@tyler_wooten @f_ash_lyn @natureforeverx'
        tag_something(post, comment)


def follow_profile(post):
    # follow profile by an id
    bot.follow(user_id=post['user_id'])


def like_picture(post):
    # like post by media id
    bot.like(media_id=post['media_id'])  # shows it isn't working, but it is


def comment_on_post(post, comment):
    # comment on post by media id
    bot.comment(media_id=post['media_id'], comment_text=comment)


def tag_something(post, comment):
    # tag on post by media id
    bot.comment(media_id=post['media_id'], comment_text=comment)

    if "friends" or "friend" in caption:
        # TODO find number of people to tag and store in friend_number
        friend_number = 1
        # print('tagged ', friend_number, ' friends.', '\n')
        # TODO tag friends




# TODO: another program that feeds this one with a post that fits the parameters

# Test with this post: https://www.instagram.com/p/BvFHV32B5mA/

# TODO: build out to paste in url and remove everything but shortcode.
#Name = input('What is the post?: ') #should name folder the name of the profile
Name = 'gothamroasters'
SHORTCODE = 'BvFHV32B5mA' # can get this from json data['node']['shortcode']

# Creating .json files of each post
# See parameters here: https://instaloader.github.io/as-module.html#instaloader-main-class
L = Instaloader(download_pictures=False, download_videos=False, download_geotags=False, compress_json=False, download_comments=False, download_video_thumbnails=False, post_metadata_txt_pattern='')
post = Post.from_shortcode(L.context, SHORTCODE)
folder_save_name = Name
# Downloads the post into a folder
download = L.download_post(post, folder_save_name)



# looks for follow, like, comment, tag


############################################################################

# TODO add into an excel file called "currently_entered.xlsx"

# opens json file for parsing
# TODO make this link dynamic
with open('C:/Users/Tyler Wooten/Documents/GitHub/Python/Instagram_Bot/gothamroasters/2019-03-16_18-52-08_UTC.json') as complex_data:
    # stores dictionary version of json file in data
    data = json.loads(complex_data.read())
    # navigates dictionary to find data we want
    caption = (data['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    post_link = ("https://www.instagram.com/p/" + data['node']['shortcode'] + '/')
    username = (data['node']['owner']['username'])
    photo_url = (data['node']['display_url'])
    user_id = (data['node']['owner']['id'])
    media_id = (data['node']['id'])
    print(media_id)

    # initialize the post dictionary
    post = {}
    # fill post dictionary with data from above
    post['username'] = username
    post['caption'] = caption
    post['post_link'] = post_link
    post['photo_url'] = photo_url
    post['user_id'] = user_id
    post['media_id'] = media_id
    check_for_actions(post)

