import argparse
import os
import traceback
from colorama import Fore, Style
from pytube import YouTube
from moviepy.audio.io.AudioFileClip import AudioFileClip


def main():
    # Pars all CLI arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('url', metavar='U', type=str, nargs='?', help='youtube video url which needs to be downloaded, like "https://www.youtube.com/watch?v=Fd_3EkGr0-4" or "https://youtu.be/Fd_3EkGr0-4"')
    parser.add_argument('mode', metavar='M', type=str, nargs='?', choices=["mp3", "mp4", "audio", "video"], default="mp4", help='download mode can be "mp3"/"mp4"/"audio"/"video"')
    parser.add_argument('-o', metavar='o', type=str, nargs='?', default="", help='output directory (optional, defaults to current working directory)')
    args = parser.parse_args()
    input_mode = args.mode
    input_url = args.url
    input_output_folder_path = args.o
    cwd_path = os.getcwd()

    # Make sure URL is valid
    if input_url is None or len(str(input_url).strip()) == 0:
        print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Please provide a valid YouTube URL like "https://www.youtube.com/watch?v=Fd_3EkGr0-4" or "https://youtu.be/Fd_3EkGr0-4"')
        exit(1)
    input_url = str(input_url)
    if not input_url.startswith("https://www.youtube.com/") and not input_url.startswith("https://youtu.be/"):
        print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Please provide a valid YouTube URL like "https://www.youtube.com/watch?v=Fd_3EkGr0-4" or "https://youtu.be/Fd_3EkGr0-4"')
        exit(2)

    # Decide where to save the video (default to current working dir)
    output_folder_path = cwd_path
    if input_output_folder_path is not None:
        input_output_folder_path = str(input_output_folder_path).strip()

        # Strip the path of trailing slashes
        if input_output_folder_path.endswith("/"):
            input_output_folder_path = input_output_folder_path[0:-1]

        # If a path was submitted
        if len(input_output_folder_path) > 0:
            # Make sure path exists
            if not os.path.exists(input_output_folder_path):
                print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Specified output directory doesn\'t exist "' + str(input_output_folder_path) + '"')
                exit(3)
            else:
                output_folder_path = input_output_folder_path

    # Download audio
    print(Fore.YELLOW + 'INFO!' + Style.RESET_ALL + ' Started downloading from "' + input_url + '"')
    youtube = YouTube(input_url)
    if input_mode in ["mp3", "audio"]:
        try:
            # Get stream
            video = youtube.streams.get_audio_only()

            # Make sure we don't overwrite anything with the output file
            output_file_path = output_folder_path + '/' + video.default_filename
            if os.path.exists(output_file_path):
                print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' File already exists at "' + output_file_path + '" and we don\'t want to accidentally overwrite it')
                raise FileExistsError()
            output_file_path = output_folder_path + '/' + video.default_filename.replace("mp4", "mp3")
            if os.path.exists(output_file_path):
                print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' File already exists at "' + output_file_path + '" and we don\'t want to accidentally overwrite it')
                raise FileExistsError()

            # Download mp4 and rename to mp3
            out_video_filepath = video.download(output_path=output_folder_path)
            base, ext = os.path.splitext(out_video_filepath)
            out_audio_filepath = base + '.mp3'
            print(Fore.GREEN + 'SUCCESS! 1/2' + Style.RESET_ALL + ' Downloaded mp4 video from "' + input_url + '" to "' + out_video_filepath + '"')

            # Make sure we convert it to mp3
            moviepy_audio_clip = AudioFileClip(out_video_filepath)
            moviepy_audio_clip.write_audiofile(out_audio_filepath, verbose=False, logger=None)
            moviepy_audio_clip.close()
            os.remove(out_video_filepath)
            print(Fore.GREEN + 'SUCCESS! 2/2' + Style.RESET_ALL + ' Converted to mp3 audio "' + out_audio_filepath + '"')
        except FileExistsError:
            exit(-1)
        except:
            traceback.print_exc()
            print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Unexpected exception occurred')
            exit(-1)

    # Download video
    elif input_mode in ["mp4", "video"]:
        try:
            # Get stream
            video = youtube.streams.get_highest_resolution()

            # Make sure we don't overwrite anything with the output file
            output_file_path = output_folder_path + '/' + video.default_filename
            if os.path.exists(output_file_path):
                print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' File already exists path "' + output_file_path + '" and we don\'t want to accidentally overwrite it')
                raise FileExistsError()

            # Download
            out_video_filepath = video.download(output_path=output_folder_path)
            print(Fore.GREEN + 'SUCCESS! 1/1' + Style.RESET_ALL + ' Downloaded mp4 video from "' + input_url + '" to "' + out_video_filepath + '"')
        except FileExistsError:
            exit(-1)
        except:
            traceback.print_exc()
            print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Unexpected exception occurred')
            exit(-1)

    # Extra error if download mode is invalid
    else:
        print(Fore.RED + 'ERROR!' + Style.RESET_ALL + ' Please provide a valid download mode like "mp3"/"mp4"/"audio"/"video"')
        exit(4)


if __name__ == "__main__":
    main()
