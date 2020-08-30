import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%d-%m-%Y %I:%M:%S %p")
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger