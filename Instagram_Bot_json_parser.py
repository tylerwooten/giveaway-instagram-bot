import json
import instabot


# looks for follow, like, comment, tag

# Test with this post: https://www.instagram.com/p/BvFHV32B5mA/

def check_for_actions(post):
    caption = post['caption'].lower()

    if 'follow' in caption:
        print('Follow found.\n')
        profile = post['username']
        follow_profile(profile, post)

    if 'like' or 'double tap' or 'double-tap' in caption:
        print('Like found.\n')
        post_to_like = post['post_link']
        like_picture(post)

    if 'comment' in caption:
        print('Comment found.\n')
        post_to_comment = post['post_link']
        comment_on_post(post)

    if 'tag' in caption:
        print('Tag found.\n')
        post_to_tag_on = post['post_link']
        tag_something(post)


def follow_profile(profile, post):
    print('Followed profile: ', profile, '\n')
    print('On post: ', post['post_link'], '\n')
    # TODO Add in functionality


def like_picture(post):
    print('Liked picture: ', post['post_link'], '\n')
    # TODO Add in functionality


def comment_on_post(post):
    print('Commented on post: ', post['post_link'], '\n')
    # TODO Add in functionality


def tag_something(post):
    print('tagged on post: ', post['post_link'], '\n')
    caption = post['caption'].lower()

    if "friends" in caption:
        # TODO find number of people to tag and store in friend_number
        friend_number = 1
        print('tagged ', friend_number, ' friends.', '\n')
        # TODO tag friends

############################################################################

# TODO need to add in looping through every json in folder

# Initializes empty list of posts
# TODO store this in an excel file or something else
list_of_posts = []

# opens json file for parsing
with open('C:/Users/Tyler Wooten/Documents/GitHub/Python/Instagram_Bot/retreataggies/2018-10-31_13-48-59_UTC.json') as complex_data:
    # stores dictionary version of json file in data
    data = json.loads(complex_data.read())
    # navigates dictionary to find data we want
    caption = (data['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    post_link = ("https://www.instagram.com/p/" + data['node']['shortcode'] + '/')
    username = (data['node']['owner']['username'])
    photo_url = (data['node']['display_url'])
    # initialize the post dictionary
    post = {}
    # fill post dictionary with data from above
    post['username'] = username
    post['caption'] = caption
    post['post_link'] = post_link
    post['photo_url'] = photo_url
    # append this post to the list of posts
    list_of_posts.append(post)

for item in list_of_posts:
    caption = post['caption'].lower()
    if "giveaway" in caption:
        print("Giveaway found.\n")
        # TODO add in alert system
        # passes post through to check_for_actions
        check_for_actions(post)

    if "free" in caption:
        print("Free found.\n")
        # TODO add in alert system
        # passes post through to check_for_actions
        check_for_actions(post)

    if "win" in caption:
        print("Win found.\n")
        # TODO add in alert system
        # passes post through to check_for_actions
        check_for_actions(post)

    else:
        check_for_actions(post)


