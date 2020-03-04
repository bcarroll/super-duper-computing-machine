import os
import sys

audio_dir = '/media/audio'
video_dir = '/media/video'
picture_dir = '/media/pictures'

audio_media = ['mp3', 'flac']
video_media = ['mp4', 'avi', 'm4v', 'mpg']
picture_media = ['png', 'jpg']

def get_files_by_type(dir, ext):
    print('scanning ' + dir + ' for files with extension: ' + ext)
    media_type = {}
    media_type[ext] = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                print('found ' + file)
                media_type[ext].append(os.path.join(root, file))
    return media_type

def get_all_media():
    media_files = {}
    audio_media = get_all_audio_media()
    if audio_media is not None:
       media_files.update(audio_media)
    
    video_media = get_all_video_media()
    if video_media is not None:
       media_files.update(video_media)
    
    picture_media = get_all_picture_media()
    if picture_media is not None:
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
        return None

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
        return None

def get_all_picture_media():
    media_files = {
        'picture': {}
    }
    for ext in picture_media:
        picture_ext_files = get_files_by_type(picture_dir, ext)
        if len(picture_ext_files[ext]) > 0:
            media_files['picture'].update(picture_ext_files)
    if len(media_files['picture'].keys()) > 0:
        return media_files
    else:
        return None