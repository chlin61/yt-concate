from .step import Step


class ReadCaptions(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('Read Captions ...')
        for yt in data:
            if not utils.cation_file_exist(yt):
                continue
        # for caption_file in os.listdir(CAPTION_DIR):
            captions = {}
            with open(yt.caption_filepath, 'r') as f:
                count = 0
                time = None
                for line in f:
                    if count % 4 == 1:
                        time = line.strip()
                    if count % 4 == 2:
                        cap = line.strip()
                        captions[cap] = time
                    count += 1
            yt.captions = captions

        return data
