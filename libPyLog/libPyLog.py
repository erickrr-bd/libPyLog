from datetime import date
from libPyUtils import libPyUtils
from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler

class libPyLog:

	def __init__(self):
		"""
		Class constructor.
		"""
		self.__utils = libPyUtils()


	def generateApplicationLog(self, message, log_level, log_name, **kwargs):
		"""
		Method that creates application logs.

		:arg message (string): Message displayed in the log
		:arg log_level (integer): Log criticality level (1 - INFO, 2 - WARNING, 3 - ERROR).
		:arg log_name (string): Log name.
		
		Keyword Args:
        	:arg use_stream_handler (boolean): If the log were created with a stream handler.
        	:arg use_file_handler (boolean): If the log were created with a file handler.
        	:arg log_file_name (string): Absolute path where the log file will be created.
        	:arg user (string): Owner user of the log file.
        	:arg group (string): Group owner of the log file.
		"""
		logger = getLogger(log_name)
		logger.setLevel(INFO)
		if (logger.hasHandlers()):
   	 		logger.handlers.clear()
		if "use_stream_handler" in kwargs and kwargs["use_stream_handler"]:
			sh = StreamHandler()
			formatter_stream_handler = Formatter('%(levelname)s - %(name)s - %(message)s')
			sh.setFormatter(formatter_stream_handler)
			logger.addHandler(sh)
		if "use_file_handler" in kwargs and kwargs["use_file_handler"]:
			path_log_file = kwargs["log_file_name"] + str(date.today()) + ".log"
			fh = FileHandler(path_log_file)
			formatter_file_handler = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
			fh.setFormatter(formatter_file_handler)
			logger.addHandler(fh)
			if "user" in kwargs and "group" in kwargs:
				self.__utils.changeFileFolderOwner(path_log_file, kwargs["user"], kwargs["group"], "640")
		if log_level == 1:
			logger.info(message)
		elif log_level == 2:
			logger.warning(message)
		elif log_level == 3:
			logger.error(message)