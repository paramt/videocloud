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

def get_cc(video_id: str, language: list) -> str:
	"""Returns captions from a YouTube video in a word-separated list"""
	try:
		captions = ytcc.get_transcript(video_id, languages=language)
	except:
		captions = ytcc.get_transcript(video_id)

	full_captions = ""

	for caption in captions:
		full_captions += caption["text"] + " "

	return full_captions.lower()

def wordcloud(words: str, font: str) -> Image:
	"""Generates a word cloud from a list of strings"""
	font = get_font(font)

	try:
		wordcloud = WordCloud(
			width = 1000,
			height = 500,
			font_path = font,
			background_color = "#d1d1d1").generate(words)
		image = wordcloud.to_image()

	except Exception:
		print(f"There was an unknown error generating the wordcloud.")
		sys.exit(1)

	finally:
		delete_font(font)

	return image

def videocloud(url: str, filepath: str, language: list, font: str):
	try:
		video_id = get_video_id(url)
		captions = get_cc(video_id, language)
		image = wordcloud(captions, font)
		image.save(filepath)

	except ytcc.CouldNotRetrieveTranscript:
		print("The specified video either doesn't exist or doesn't have captions enabled. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)
	except IOError:
		print(f"There was an error saving the wordcloud file. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)

	return os.path.abspath(filepath)

def main():
	try:
		video_id = sys.argv[1]
	except:
		print("Please specify a YouTube video link or video ID. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)

	try:
		filepath = sys.argv[2]
	except IndexError:
		filepath = "wordcloud.png"

	try:
		language = [sys.argv[3]]
	except IndexError:
		language = ["en"]

	try:
		font = sys.argv[4]
	except IndexError:
		font = "https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true"

	wordcloud = videocloud(video_id, filepath, language, font)
	print(f"Wordcloud created in {wordcloud}")
