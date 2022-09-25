


# pip install urllib
# pip install m3u8
# pip install streamlink
import urllib
import m3u8
import streamlink
from subprocess import check_output
import subprocess   

def has_audio_streams(file_path):
    command = ["ffmpeg", "-i", file_path, "-af",  "ebur128=framelog=verbose",  "-f", "null", "-"]

    output = check_output(command, stderr=subprocess.STDOUT);

    return float(str(output).split("I:         ")[1].split(" ")[0]) < 60

def get_stream(url):
    """
    Get upload chunk url
    """
    streams = streamlink.streams(url)
    stream_url = streams["best"]

    m3u8_obj = m3u8.load(stream_url.args['url'])
    return m3u8_obj.segments[0]


def dl_stream(url, filename, chunks):
    """
    Download each chunks
    """
    pre_time_stamp = 0
    for i in range(chunks+1):
        stream_segment = get_stream(url)
        cur_time_stamp = \
            stream_segment.program_date_time.strftime("%Y%m%d-%H%M%S")

        if pre_time_stamp == cur_time_stamp:
            pass
        else:
            print(cur_time_stamp)
            saveAs = filename + '_' + str(cur_time_stamp) + '.ts'
            file = open(saveAs, 'ab+')
            with urllib.request.urlopen(stream_segment.uri) as response:
                html = response.read()
                file.write(html)
            pre_time_stamp = cur_time_stamp
            print("  Has audio: ", has_audio_streams(saveAs))


# url = "https://www.youtube.com/watch?v=2U3JnFbD-es"
url = "https://www.youtube.com/watch?v=_KdmrB9a0rs"
url = "https://www.youtube.com/watch?v=JRuSPazlAuc"
dl_stream(url, "live", 15)