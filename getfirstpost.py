import os
import instaloader

def getfirstpost():

    bot = instaloader.Instaloader()
    bot.login(USER, PASS)

    posts = instaloader.Profile.from_username(bot.context, 'spiritedvirginia').get_posts()

    outputdirectory = (/tmp)

    os.chdir(outputdirectory)

    bot.download_post(posts.first_item, "spiritedvirginia")