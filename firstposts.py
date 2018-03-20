from sys import argv
import webbrowser
import praw
import yaml
import datetime
import time


def main(subreddit, daysaftercreated):

    # Convert daysaftercreated to an integer blurts error if doesn't. 
    daysaftercreated = int(daysaftercreated)

    # Load reddit configuration as dictionary
    yamlfile = yaml.load(open('config.yml', 'r'))

    # Reddit login info from yaml 
    reddit = praw.Reddit(client_id = yamlfile['client_id'],
        client_secret = yamlfile['client_secret'],
        user_agent = yamlfile['user_agent'])

    # Create subreddit instance 
    subreddit_instance = reddit.subreddit(subreddit)

    # Retrives date created from instance
    sub_createdate_unix = int(subreddit_instance.created_utc)

    # Convert to dt, add requested time, convert back to unix
    sub_createdate_dt = datetime.datetime.fromtimestamp(sub_createdate_unix) 
    new_time_dt = (sub_createdate_dt + datetime.timedelta(days=daysaftercreated)) 
    new_time_unix = time.mktime(new_time_dt.timetuple())

    url = "https://reddit.com/r/%s/search?sort=new&q=timestamp%%3A%d..%d&restrict_sr=on&syntax=cloudsearch" % (
            subreddit, sub_createdate_unix, new_time_unix)
    return url
