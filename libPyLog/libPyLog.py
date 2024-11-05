"""
Author: Erick Roberto Rodriguez Rodriguez
Email: erodriguez@tekium.mx, erickrr.tbd93@gmail.com
GitHub: https://github.com/erickrr-bd/libPyLog
libPyLog v2.1 - October 2024
"""
from datetime import date
from libPyUtils import libPyUtils
from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler

class libPyLog:

	def __init__(self):
		"""
		Class constructor.
		"""
		self.utils = libPyUtils()


	def create_log(self, message, level, name, **kwargs):
		"""
		Method that creates logs.

		:arg message (string): Log's message.
		:arg level (integer): Criticality level.
		:arg name (string): Log's name.
		
		Keyword Args:
        	:arg use_stream_handler (boolean): Option to create a log that is only displayed on the screen.
        	:arg use_file_handler (boolean): Option to create a log file.
        	:arg file_name (string): Log file path.
        	:arg user (string): Owner user.
        	:arg group (string): Group owner.
        """
		logger = getLogger(name)
		logger.setLevel(INFO)
		if(logger.hasHandlers()):
			logger.handlers.clear()
		if "use_stream_handler" in kwargs and kwargs["use_stream_handler"]:
			stream_handler = StreamHandler()
			stream_handler_format = Formatter('%(levelname)s - %(name)s - %(message)s')
			stream_handler.setFormatter(stream_handler_format)
			logger.addHandler(stream_handler)
		if "use_file_handler" in kwargs and kwargs["use_file_handler"]:
			log_file = kwargs["file_name"] + '-' + str(date.today()) + ".log"
			file_handler = FileHandler(log_file)
			file_handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
			file_handler.setFormatter(file_handler_format)
			logger.addHandler(file_handler)
			if "user" in kwargs and "group" in kwargs:
				self.utils.change_owner(log_file, kwargs["user"], kwargs["group"], "640")
		match level:
			case 1:
				logger.debug(message)
			case 2:
				logger.info(message)
			case 3:
				logger.warning(message)
			case 4:
				logger.error(message)
			case 5:
				logger.critical(message)