
from pytube import YouTube
from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Download Captions...')
        for yt in data:
            logger.info('downloading cation for ' + yt.url)
            if utils.cation_file_exist(yt):
                logger.debug('found existing caption file: ' + yt.get_caption_filepath())
                continue

            try:
                source = YouTube(yt.url)
                # print(source.captions.all())
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                logger.error('Error : When downloading caption for ' + yt.url)
                continue
            # print(en_caption_convert_to_srt)
            # # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(yt.url), 'w', encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        return data



