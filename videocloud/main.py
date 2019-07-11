import logging
import os
import sys
import urllib.request
import click
import numpy as np
import PIL.Image as Image
from wordcloud import WordCloud
from youtube_transcript_api import YouTubeTranscriptApi as ytcc

# Mute youtube_transcript_api stdout
logging.disable(logging.CRITICAL)

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

	except:
		print(f"There was an unknown error generating the videocloud.")
		sys.exit(1)

	finally:
		delete(font, mask)

	return image

@click.command()
@click.option("--url", type=str, help="Link to a YouTube video", required=True)
@click.option("--filepath", default="videocloud.png", help="Where on the disk to save the videocloud")
@click.option("--language", default="en", help="Language code of the captions")
@click.option("--font",
              default="https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true",
			  help="Link to a TTF font file")
@click.option("--mask",
              default="https://github.com/paramt/videocloud/blob/master/assets/masks/cloud.png?raw=true",
			  help="Link to a PNG mask file")

def videocloud(url: str, filepath:str, language: list, font: str, mask: str):
	try:
		video_id = get_video_id(url)
		captions = get_cc(video_id, [language])
		image = wordcloud(captions, font, mask)

	except ytcc.CouldNotRetrieveTranscript:
		print("The specified video either doesn't exist or doesn't have captions enabled. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)
	except IOError:
		print(f"There was an error saving the videocloud. For more help visit https://www.param.me/videocloud#usage")
		sys.exit(1)

	image.save(filepath)

	filepath = os.path.abspath(filepath)
	print(f"Videocloud created in {filepath}")
