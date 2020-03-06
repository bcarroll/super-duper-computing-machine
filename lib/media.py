import os
import sys
from conf.config import Media
import logging

logger = logging.getLogger(__name__)

audio_dir = Media.audio_dir
video_dir = Media.video_dir
picture_dir = Media.picture_dir

audio_media = Media.audio_media
video_media = Media.video_media
picture_media = Media.picture_media

def get_files_by_type(dir, ext):
    logger.debug('scanning ' + dir + ' for files with extension: ' + ext)
    media_type = {}
    media_type[ext] = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                logger.debug('found ' + file)
                media_type[ext].append(os.path.join(root, file))
    return media_type

def get_all_media():
    media_files = {}
    audio_media = get_all_audio_media()
    if len(audio_media).keys > 0:
       media_files.update(audio_media)
    
    video_media = get_all_video_media()
    if len(video_media).keys > 0:
       media_files.update(video_media)
    
    picture_media = get_all_picture_media()
    if len(picture_media).keys > 0:
       media_files.update(picture_media)
    
    return media_files

def get_all_audio_media():
    media_files = {
        'audio': {}
    }
    for ext in audio_media:
        audio_ext_files = get_files_by_type(audio_dir, ext)
        if len(audio_ext_files[ext]) > 0:
            media_files['audio'].update(audio_ext_files)
    if len(media_files['audio'].keys()) > 0:
        return media_files
    else:
        return {}

def get_all_video_media():
    media_files = {
        'video': {}
    }
    for ext in video_media:
        video_ext_files = get_files_by_type(video_dir, ext)
        if len(video_ext_files[ext]) > 0:
            media_files['video'].update(video_ext_files)
    if len(media_files['video'].keys()) > 0:
        return media_files
    else:
        return {}

def get_all_picture_media():
    media_files = {
        'picture': {}
    }
    for ext in picture_media:
        picture_ext_files = get_files_by_type(picture_dir, ext)
        if len(picture_ext_files[ext]) > 0:
            logger.debug('Adding image files in %s to dict' % picture_dir)
            media_files['picture'].update(picture_ext_files)
        else:
            logger.debug('No image files found in %s' % picture_dir)
    if len(media_files['picture'].keys()) > 0:
        logger.debug('Returning dict with image files in %s' % picture_dir)
        return media_files
    else:
        logger.debug('Returning None')
        return {}