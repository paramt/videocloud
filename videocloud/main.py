import os
import sys
import PIL.Image as Image
from wordcloud import WordCloud
from youtube_transcript_api import YouTubeTranscriptApi as ytcc
import urllib.request
import numpy as np

def download(url: str, filepath: str) -> str:
	try:
		urllib.request.urlretrieve(url, filepath)
	except:
		print("Unable to download the needed assets to generate the videocloud")
		print("Please make sure that you have provided the correct URLs to any fonts/masks")
		sys.exit(1)
	else:
		return filepath

def delete(*files) -> bool:
	for f in files:
		try:
			os.remove(f)
		except:
			print(f"Unable to remove {f} while cleaning up")

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

def wordcloud(words: str, font: str, mask: str) -> Image.Image:
	"""Generates a word cloud from a list of strings"""
	font = download(font, "tempfont.ttf")
	mask = download(mask, "tempmask.png")
	mask_data = np.array(Image.open(mask))

	try:
		wordcloud = WordCloud(
			width = 1000,
			height = 500,
			font_path = font,
			background_color = "#d1d1d1",
			mask = mask_data,
		).generate(words)

		image = wordcloud.to_image()

	except Exception:
		print(f"There was an unknown error generating the videocloud.")
		sys.exit(1)

	finally:
		delete(font, mask)

	return image

def videocloud(url: str, filepath: str, language: list, font: str, mask: str):
	try:
		video_id = get_video_id(url)
		captions = get_cc(video_id, language)
		image = wordcloud(captions, font, mask)
		image.save(filepath)

	except ytcc.CouldNotRetrieveTranscript:
		print("The specified video either doesn't exist or doesn't have captions enabled. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)
	except IOError:
		print(f"There was an error saving the videocloud. For more help visit https://www.param.me/videocloud#usage")
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
		filepath = "videocloud.png"

	try:
		language = [sys.argv[3]]
	except IndexError:
		language = ["en"]

	try:
		font = sys.argv[4]
	except IndexError:
		font = "https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true"

	try:
		mask = sys.argv[5]
	except IndexError:
		mask = "https://github.com/paramt/videocloud/blob/master/assets/masks/cloud.png?raw=true"

	wordcloud = videocloud(video_id, filepath, language, font, mask)
	print(f"Videocloud created in {wordcloud}")
