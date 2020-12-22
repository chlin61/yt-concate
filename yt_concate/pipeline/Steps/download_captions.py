# from youtube_transcript_api import YouTubeTranscriptApi

from pytube import YouTube
from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for url in data:
            print('downloading cation for ', url)
            if utils.cation_file_exist(url):
                print('found existing caption file: ', utils.get_caption_filepath(url))
                continue

            try:
                source = YouTube(url)
                # print(source.captions.all())
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print('Error : When downloading caption for ', url)
                continue
            # print(en_caption_convert_to_srt)
            # # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(url), 'w', encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        # return data



    # def process1(self, data, inputs):
    #     for url in data:
    #         video_id = url.split('v=')[-1]
    #         str = YouTubeTranscriptApi.get_transcript(video_id)  # lis[dic('text、star、duration')]
    #


