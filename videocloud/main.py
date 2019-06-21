import os
import sys
from PIL.Image import Image
from wordcloud import WordCloud
from youtube_transcript_api import YouTubeTranscriptApi as ytcc
import urllib.request

def get_font(url: str) -> str:
	filepath = "tempfont.ttf"
	urllib.request.urlretrieve(url, filepath)
	return filepath

def delete_font(filepath: str) -> bool:
	try:
		os.remove(filepath)
	except:
		return False
	else:
		return True

def get_video_id(url: str) -> str:
    return(url[-11:])

def get_cc(video_id: str) -> str:
	"""Returns captions from a YouTube video in a word-separated list"""
	try:
		captions = ytcc.get_transcript(video_id, languages=["en"])
	except:
		captions = ytcc.get_transcript(video_id)

	full_captions = ""

	for caption in captions:
		full_captions += caption["text"] + " "

	return full_captions.lower()

def wordcloud(words: str) -> Image:
	"""Generates a word cloud from a list of strings"""
	font = get_font("https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true")

	try:
		wordcloud = WordCloud(
			width = 1000,
			height = 500,
			font_path = font,
			background_color = "#d1d1d1").generate(words)
		image = wordcloud.to_image()

	except Exception as e:
		print(f"There was an error generating the wordcloud: {e}")
		exit()

	finally:
		delete_font(font)

	return image

def videocloud(url: str, filepath):
	try:
		video_id = get_video_id(url)
		captions = get_cc(video_id)
		image = wordcloud(captions)
		image.save(filepath)

	except ytcc.CouldNotRetrieveTranscript:
		print("The specified video either doesn't exist or doesn't have captions enabled. Please try again")
		exit()
	except IOError as e:
		print(f"There was an error saving the wordcloud file: {e}")
		exit()

	return os.path.abspath(filepath)

def main():
	try:
		video_id = sys.argv[1]
	except:
		print("Please specify a YouTube video link or video ID")
		exit()

	try:
		filepath = sys.argv[2]
	except IndexError:
		filepath = "wordcloud.png"

	wordcloud = videocloud(video_id, filepath)
	print(f"Wordcloud created in {wordcloud}")
