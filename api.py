import flask
from flask import Response, request
from src.main import main
from werkzeug.exceptions import BadRequest
from youtube_transcript_api import YouTubeTranscriptApi as ytcc
import random

app = flask.Flask(__name__)

@app.errorhandler(BadRequest)
def handle_invalid_ytid(e):
	return Response("{'status': 400, 'reason': A valid YouTube video ID has not been provided}", status = 400, mimetype = 'application/json')

@app.errorhandler(ytcc.CouldNotRetrieveTranscript)
def handle_missing_caption(e):
	return Response("{'status': 400, 'reason': The video either does not exist or does not have captions enabled}", status = 400, mimetype = 'application/json')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
	try:
		vid = request.args["video_id"]
		out = f"out/{vid[-11:]}.png"
		wordcloud = main(vid, out)
		filepath = request.base_url + wordcloud
		return Response(f"'status': 201, 'video': {vid}, 'wordcloud': {filepath}", status = 201, mimetype = 'application/json')
	except Exception as e:
		return Response(f"Error 502: {e}", status = 502, mimetype = 'application/json')
