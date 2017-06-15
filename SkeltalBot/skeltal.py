'''
	SkeltalBot:
	Small bot to help me learn the basics of the reddit api
	Basically, look at some subreddits, look for comments with
	a variant of the phrase "Thank Mr. Skeltal", and respond with some variant
	of "Doot Doot"

	Dead simple, and mainly a teaching thing.
	Don't worry, I'll be doing a more complex reddit bot soon
'''

import praw
import pdb
import re
import os

reddit = praw.reddit('bot1')
subreddit = reddit.subreddit('ledootgeneration', 'fullcommunism')

# Just to make sure that I'm getting the right info
# print out the current hot submissions

for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Score: ", submission.score)
	print("\n")

# Now, sift through the content of the post. If there's any
# text that says "Thank Mr. Skeltal", post a comment with a
# variant of the phrase "Doot Doot"

# Once that's done, sift through the comments in the thread
# Find a variant of "Thank Mr. Skeltal", and return variant
# of "Doot Doot"