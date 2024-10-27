import logging
from fileinput import filename


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\logs\\automation.log",format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        # print("logs generated")
        # logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)
        # Create a named logger
        logger = logging.getLogger(__name__)

        # Create a file handler
        filehandler = logging.FileHandler('.//logs//logfile.log')

        # Set the formatter for the file handler
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        # logger.debug("Debug statement is executed")
        # logger.info("Information statement is executed")
        # logger.warning("Warning mode, but test continues")
        # logger.error("Error has happened and failed the test")
        # logger.critical("Critical issue")
        return logger
