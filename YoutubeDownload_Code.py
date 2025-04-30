import yt_dlp

def video_downloader(url):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'forcejson': True,
            'skip_download': True,
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            direct_url = info['url']  # direct link to media stream
            return direct_url,info
    except yt_dlp.utils.DownloadError:pass

    return "invalidUrl"


def get_audio_url(video_url):
    # Define options for yt_dlp
    ydl_opts = {
        'forcejson': True,
        'quiet': True,  # Suppress regular output
        'skip_download': True,  # Don't download, just extract info
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Extract info about the video
        info = ydl.extract_info(video_url, download=False)

        # Search for the audio formats by checking for known audio extensions
        for format in info.get('formats', []):
            # Check if it's an audio format by looking at the extension
            if format.get('acodec') and 'audio' in format['acodec']:
                return format['url'],info

            # Alternatively, check the extension for audio-only formats (e.g., m4a, opus, webm)
            if format['ext'] in ['mp3', 'm4a', 'opus', 'webm']:
                return format['url'],info  # Return the direct audio URL

    return None  # If no
