import logging
from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from lib.media import get_all_media, get_all_audio_media, get_all_video_media, get_all_picture_media

logger = logging.getLogger(__name__)
api_media = Blueprint('api_media', __name__, template_folder='templates')

@api_media.route('/api/v1/media/')
def api_get_all_media():
    logger.debug('Returning all media')
    all_media = get_all_media()
    return jsonify(all_media)

@api_media.route('/api/v1/media/audio/')
def api_get_all_audio_media():
    logger.debug('Returning all audio media')
    return jsonify(get_all_audio_media())

@api_media.route('/api/v1/media/video/')
def api_get_all_video_media():
    logger.debug('Returning all video media')
    return jsonify(get_all_video_media())

@api_media.route('/api/v1/media/picture/')
def api_get_all_picture_media():
    logger.debug('Returning all picture media')
    return jsonify(get_all_picture_media())