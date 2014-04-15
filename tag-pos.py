import json
import sys
import nltk

def process_tweet(input_tweet):
	tweet_json = json.loads(input_tweet)

	# get tweet text
	tweet_text = tweet_json['text']

	# tokenize and label parts of speech
	tokens = nltk.word_tokenize(tweet_text)

	tagged = nltk.pos_tag(tokens)

	# add tagged parts of speech to JSON
	output_tweet = {'id': tweet_json['id'], 'coordinates': tweet_json['coordinates'], 'created_at': tweet_json['created_at'], 'user': {'id': tweet_json['user']['id'], 'screen_name': tweet_json['user']['screen_name']}, 'text': tweet_text, 'pos_tags': tagged}

	return output_tweet

def process_file(input_filename, output_filename):
	"""
	Process the file one input at a time and write the given output file
	"""
	# Create output file
	outfile = open(output_filename, 'w')

	# Process one line of the file
	with open(input_filename, 'r') as infile:
		for line in infile:
			tweet_output = process_tweet(line)
			if tweet_output is not None:
				json.dump(tweet_output, outfile)
				outfile.write('\n')

		infile.close()

	outfile.close()

if __name__ == '__main__':

	# Get arguments
	arguments = sys.argv
	arguments_len = len(arguments)

	# Data set name 
	input_filename = arguments[1]
	output_filename = arguments[2]
	process_file(input_filename, output_filename)