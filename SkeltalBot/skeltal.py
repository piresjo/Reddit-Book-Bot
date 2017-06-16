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

if not os.path.isfile("posts_replied_to.txt"):
	postsRepliedTo = [];
else:
	with open("posts_replied_to.txt", "r") as file:
		postsRepliedTo = file.read()
		postsRepliedTo = postsRepliedTo.split("\n")
		postsRepliedTo = list(filter(None, postsRepliedTo))

if not os.path.isfile("comments_replied_to.txt"):
	commentsRepliedTo = [];
else:
	with open("comments_replied_to.txt", "r") as file:
		commentsRepliedTo = file.read()
		commentsRepliedTo = commentsRepliedTo.split("\n")
		commentsRepliedTo = list(filter(None, commentsRepliedTo))

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
	# Also, go through comments

	# Get the comments and flatten them
	submission.comments.replace_more(limit=0)
	comments = submission.comments.list()
	# First off, go through comments. Any instance of 'thank mr. skeltal'
	# will need to be commented
	for comment in comments:
		if comment.id not in commentsRepliedTo:
			if re.search("thank mr. skeltal", comment.body, re.IGNORECASE):
				comment.reply("Doot Doot")
				print("Bot replying to : ", comment.id)
				commentsRepliedTo.append(comment.id)
			elif re.search("thank comrade skeltal", comment.body, re.IGNORECASE):
				comment.reply("Doot Doot")
				print("Bot replying to : ", comment.id)
				commentsRepliedTo.append(comment.id)
			else:
				continue
	# Now the actual submission itself
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

	
# for future use, place the ids of the posts and comments
# that have already been responded to into text files. That
# way, no extra comments get posted

with open("posts_replied_to.txt", "w") as file:
	for postID in postsRepliedTo:
		file.write(postID + "\n")

with open("comments_replied_to.txt", "w") as file:
	for commentID in commentsRepliedTo:
		file.write(commentID + "\n")

# in hindsight, this is rather easy. If I was doing this
# last year, and knew about scikit, I could have done
# the phone charger bot
