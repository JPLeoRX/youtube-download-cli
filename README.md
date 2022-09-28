# YouTube Download CLI 
An elegant CLI tool built in Python that allows you to download videos from YouTube both as MP4 video files and as MP3 audio files. 

# Usage
I tried to keep it as basic as possible, after installation the tool can be accessed from terminal. You need to specify a YouTube URL for download. An optional mode to switch between video & audio (mp4 or mp3) downloads. And an optional output directory path. By default all downloaded files will be saved in current working directory from which you launched this script.

This tool was tested on MacOS and Ubuntu, and probably won't work on Windows.
### Help
```bash
leo@c6p2 ~ % youtube-download-cli -h

usage: youtube-download-cli [-h] [-o [o]] [U] [M]

positional arguments:
  U           youtube video url which needs to be downloaded, like "https://www.youtube.com/watch?v=Fd_3EkGr0-4" or "https://youtu.be/Fd_3EkGr0-4"
  M           download mode can be "mp3"/"mp4"/"audio"/"video"

optional arguments:
  -h, --help  show this help message and exit
  -o [o]      output directory (optional, defaults to current working directory)

```

### Download as MP4 video
```bash
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4"
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" mp4
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" video
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" -o "/Users/leo/Downloads"
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" mp4 -o "/Users/leo/Downloads"
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" video -o "/Users/leo/Downloads"
```
### Download as MP3 audio
```bash
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" mp3
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" audio
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" mp3 -o "/Users/leo/Downloads"
youtube-download-cli "https://www.youtube.com/watch?v=Fd_3EkGr0-4" audio -o "/Users/leo/Downloads"
```

# Installation
 
## Normal installation

```bash
pip install youtube-download-cli
```

## Development installation

```bash
git clone https://github.com/jpleorx/youtube-download-cli.git
cd youtube-download-cli
pip install --editable .
```

# Links
In case you’d like to check my other work or contact me:
* [Personal website](https://tekleo.net/)
* [GitHub](https://github.com/jpleorx)
* [PyPI](https://pypi.org/user/JPLeoRX/)
* [DockerHub](https://hub.docker.com/u/jpleorx)
* [Articles on Medium](https://medium.com/@leo.ertuna)
* [LinkedIn (feel free to connect)](https://www.linkedin.com/in/leo-ertuna-14b539187/)