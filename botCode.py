import praw
import time
from pprint import pprint

# Reddit bot is an instance of the Reddit class provided by praw
reddit_bot = praw.Reddit(user_agent='RedditBot426 v0.1',
                  client_id='mXTCjODSk62Zeg',
                  client_secret='RUl-LK40XqBeOEa1-vIw54uVI2Q',
                  username='RedditBot426',
                  password='redditbot426')

print('Current user account logged into: ', end='')
print(reddit_bot.user.me())

already_known = []

# Words to be searched in the __ current topmost hot submissions on Reddit
searchWords = []
# Subreddit to search on
searchSub = input('Which subreddit would you like to search? >> /r/')

while True:
    new_keyword = input('[Input N to stop entering keywords] \nEnter a new keyword to search for:')
    if new_keyword.lower() == 'n':
        break
    else:
        searchWords.append(new_keyword)

searchLimit = int(input('Enter the limit on how many posts you would like to search: '))

print('\nSearching for the following keywords:')
print(searchWords)
print('in top {} hot posts on the subreddit /r/{}.'.format(searchLimit, searchSub),end='\n\n\n')


while True:
    subreddit = reddit_bot.subreddit(searchSub)
    for submission in subreddit.hot(limit=searchLimit):
        text = submission.selftext.lower()
        # Searches for keywords in both the submission title and text body
        has_keyword = any(string in text for string in searchWords) \
                      or any(string in submission.title for string in searchWords)
        # Test if it contains a keyword from searchWords list
        if submission.id not in already_known and has_keyword:
            # submission.reply(...)
            # pprint(dir(submission))
            # print(submission.selftext)
            print(submission.title)
            print('Posted by u/{} in subreddit /r/{}.'.format(submission.author, submission.subreddit))
            print(submission.shortlink, end='\n\n')

            already_known.append(submission.id)
    time.sleep(10)
