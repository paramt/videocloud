from PIL.Image import Image
from wordcloud import WordCloud
from youtube_transcript_api import YouTubeTranscriptApi as ytcc
from videocloud import constants

def get_video_id(url: str) -> str:
    return(url[-11:])

def get_captions(video_id: str) -> str:
	"""Returns captions from a YouTube video in a word-separated list"""
	captions = ytcc.get_transcript(video_id)
	full_captions = ""

	for caption in captions:
		full_captions += caption["text"] + " "

	return full_captions.lower()

def generate_word_cloud(words: str) -> Image:
    """Generates a word cloud from a list of strings"""
    wordcloud = WordCloud(
        width = 1000,
        height = 500,
        font_path = f"assets/fonts/{constants.FONT}",
        background_color = constants.BG).generate(words)
    image = wordcloud.to_image()
    return image
