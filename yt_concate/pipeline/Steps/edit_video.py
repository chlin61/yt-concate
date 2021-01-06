from moviepy.editor import VideoFileClip
from moviepy.editor import CompositeVideoClip
from moviepy.editor import TextClip
from moviepy.editor import concatenate_videoclips

from .step import Step
from .step import StepException


def annotate(chip, txt, txt_color='white', font_size=20):
    txt_clip = TextClip(txt, fontsize=font_size, color=txt_color)
    cvc = CompositeVideoClip([chip, txt_clip.set_position(("center", "bottom"))])
    return cvc.set_duration(chip.duration)
# 未安装ImageMagick应用
# ImageMagick是一套功能强大、稳定而且开源的多平台工具集和开发包，可以用来读、写和处理超过200种基本格式的图片文件，包括PNG，JPEG，GIF，HEIC，TIFF，DPX，EXR，WebP，Postscript，PDF和SVG等格式。利用ImageMagick，可以根据web应用程序的需要动态生成图片, 还可以对一个(或一组)图片进行改变大小、旋转、锐化、减色或增加特效等操作，并将操作的结果以相同格式或其它格式保存，对图片的操作，既可以通过命令行进行，也可以通过C/C++、Perl、Java、PHP、Python或Ruby编程来完成。ImageMagic的主要精力集中在性能，减少bug以及提供稳定的API和ABI上。
# ImageMagick的功能通常通过命令行使用，也可以通过编程来使用。moviepy使用的方式就是通过命令行方式调用的。因此在使用TextClip前，必须安装独立的ImageMagick应用，该应用对应官方下载地址为：
# http://www.imagemagick.org/script/index.php，该网站从国内访问非常慢，老猿好不容易才弄到该工具包的windows 64位16通道图像处理的版本放在CSDN的资源服务器上，如果大家需要使用该版本可以从CSDN的资源服务器对应链接下载，下载地址为：https://download.csdn.net/download/LaoYuanPython/12539159，不过需要5个CSDN积分，但下载快，下载后解压直接点击执行文件运行即可。
#
# 安装ImageMagick没有修改moviepy的配置文件config_defaults.py
# 安装ImageMagick后，需要修改moviepy的config_defaults.py模块的配置，将下行代码：
# IMAGEMAGICK_BINARY = os.getenv('IMAGEMAGICK_BINARY', 'auto-detect')
# 替换为：
# IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-7.0.8-Q16\magick.exe"
# 具体的替换值需要确认ImageMagick安装目录进行更改。


class EditVideo(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Editting Video ...')
        video_set =[]
        for found in data:
            time = found.time
            caption = found.caption
            start, end = self.parse_caption_time(time)
            # print(found.yt.video_filepath)
            if not found.yt.check_file_exists():
                logger.debug(found.yt.video_filepath + ' 檔案沒下載成功..')
                continue
            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            video = annotate(video, caption)
            video_set.append(video)
            if len(video_set) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(video_set)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        # print(output_filepath)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, time):
        start, end = time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time):
        hh, mm, ss = time.split(':')
        ss, ms = ss.split(',')
        return int(hh), int(mm), int(ss) + int(ms) / 1000


