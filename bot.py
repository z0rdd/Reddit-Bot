import praw
import time
import os
import db


class Bot:

    def __init__(self, keyword):
        self.keyword = keyword
        self.running_on_heroku = False
        if os.environ.get("R_LOGIN") is not None:
            self.running_on_heroku = True
        print(self.running_on_heroku)
        self.database = db.Database(self.running_on_heroku)

    def login(self):

        """ login to reddit using either local config file or heroku env variables"""

        print("Logging in...")
        if self.running_on_heroku:
            reddit = praw.Reddit(username=os.environ["R_USERNAME"],
                                 password=os.environ["R_PASSWORD"],
                                 client_id=os.environ["R_CID"],
                                 client_secret=os.environ["R_SECRET"],
                                 user_agent="my test bot")
        else:
            import config
            reddit = praw.Reddit(username=config.username,
                                 password=config.password,
                                 client_id=config.client_id,
                                 client_secret=config.secret,
                                 user_agent="my test bot")
        print("Logged in !")
        return reddit

    def run_bot(self, reddit):

        """ run the bot """

        print("Doing the thing!")
        for comment in reddit.subreddit('dota2').comments(limit=100):
            if self.keyword in comment.body.lower():
                if self.database.search_comment_id(comment.id) is not None:
                    pass
                else:
                    self.database.insert(comment.id, comment.author.name, 1)

        print(self.database.view_all())
        time.sleep(20)


if __name__ == "__main__":
    bot = Bot("osfrog")
    if bot.running_on_heroku is True:
        bot.run_bot(bot.login())
    else:
        while True:
            bot.run_bot(bot.login())
