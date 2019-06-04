from src.utilities import get_video_id, generate_word_cloud as word_cloud, get_captions as get_cc

def main(url: str, filepath="out/test.png"):
	video_id = get_video_id(url)
	captions = get_cc(video_id)
	image = word_cloud(captions)
	image.save(filepath)
	return filepath

if __name__ == "__main__":
	print("Please enter the link to a YouTube video")
	main(input())
