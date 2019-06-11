import os
import sys
from VideoCloud.utilities import get_video_id, generate_word_cloud as word_cloud, get_captions as get_cc
from youtube_transcript_api import YouTubeTranscriptApi as ytcc


def main(url: str, filepath):
	try:
		video_id = get_video_id(url)
		captions = get_cc(video_id)
		image = word_cloud(captions)
		image.save(filepath)
	except ytcc.CouldNotRetrieveTranscript:
		print("The specified video either doesn't exist or doesn't have captions enabled. Please try again")
		exit()
	except IOError:
		print("There was an error saving the wordcloud file")
		exit()

	return os.path.abspath(filepath)

if __name__ == "__main__":
	try:
		video_id = sys.argv[1]
	except:
		print("Please specify a YouTube video link or video ID")
		exit()

	try:
		filepath = sys.argv[2]
	except IndexError:
		filepath = "wordcloud.png"

	wordcloud = main(video_id, filepath)
	print(f"Wordcloud created in {wordcloud}")
