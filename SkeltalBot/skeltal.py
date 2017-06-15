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

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('lebotgeneration')

if not os.path.isfile("postsRepliedTo.txt"):
	postsRepliedTo = [];
else:
	with open("posts_replied_to.txt", "r") as file:
		postsRepliedTo = file.read()
		postsRepliedTo = postsRepliedTo.split("\n")
		postsRepliedTo = list(filter(None, postsRepliedTo))

# Just to make sure that I'm getting the right info
# print out the current hot submissions

for submission in subreddit.hot(limit=10):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Score: ", submission.score)
	print("\n")
	# Now, sift through the content of the post. If there's any
	# text that says "Thank Mr. Skeltal", post a comment with a
	# variant of the phrase "Doot Doot"
	if submission.id not in postsRepliedTo:
		if re.search("thank mr. skeltal", submission.title, re.IGNORECASE):
			submission.reply("Doot Doot")
			print("Bot replying to : ", submission.title)
			postsRepliedTo.append(submission.id)
		elif re.search("thank mr. skeltal", submission.selftext, re.IGNORECASE):
			submission.reply("Doot Doot")
			print("Bot replying to : ", submission.title)
			postsRepliedTo.append(submission.id)
		else:
			continue


with open("posts_replied_to.txt", "w") as file:
	for postID in postsRepliedTo:
		file.write(postID + "\n")

# Once that's done, sift through the comments in the thread
# Find a variant of "Thank Mr. Skeltal", and return variant
# of "Doot Doot"