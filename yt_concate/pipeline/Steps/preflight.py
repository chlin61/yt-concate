
from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils, logger):
        # print('in Preflight')
        logger.info('---------------')
        logger.info('process start...')
        logger.info('Preprocess')
        utils.create_dir()
        # logger.info('程式開始執行')


