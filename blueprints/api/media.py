from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from lib.media import get_all_media, get_all_audio_media, get_all_video_media, get_all_picture_media

api_media = Blueprint('api_media', __name__, template_folder='templates')

@api_media.route('/api/v1/media')
@api_media.route('/api/v1/media/')
def api_get_all_media():
    all_media = get_all_media()
    return jsonify(all_media)

@api_media.route('/api/v1/media/audio')
@api_media.route('/api/v1/media/audio/')
def api_get_all_audio_media():
    return jsonify(get_all_audio_media())

@api_media.route('/api/v1/media/video')
@api_media.route('/api/v1/media/video/')
def api_get_all_video_media():
    return jsonify(get_all_video_media())

@api_media.route('/api/v1/media/picture')
@api_media.route('/api/v1/media/picture/')
def api_get_all_picture_media():
    return jsonify(get_all_picture_media())