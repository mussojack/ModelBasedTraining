import datetime
import logging


class logger:
    logger = None

    def myLogger(self):
        if self.logger is None:
            logging.addLevelName(35, "FAIL")
            self.logger = logging.getLogger('mainlogger')
            self.logger.setLevel(logging.INFO)
            formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.propagate = 0

        return self.logger

log = logger().myLogger()