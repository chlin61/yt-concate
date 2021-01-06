from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils, logger):
        # print('postflight')
        logger.info('process is end..')