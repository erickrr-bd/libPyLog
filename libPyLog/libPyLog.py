from datetime import date
from libPyUtils import libPyUtils
from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler

class libPyLog:

	def __init__(self):
		"""
		Method that corresponds to the constructor of the class.
		"""
		self.__utils = libPyUtils()


	def generateApplicationLog(self, message, log_level, name_log, **kwargs):
		"""
		Method that generates an application log

		:arg message (string): Message displayed in the log
		:arg log_level (integer): Level of the log (INFO, WARNING, ERROR)
		:arg name_log (string): Name that appears in the log
		
		Keyword Args:
        	:arg use_stream_handler (boolean): If the stream type log was used 
        	:arg use_file_handler (boolean): If the file type log is used
        	:arg name_file_log (string): Log path in case to use a file type log
        	:arg user (string): Username to belongs the file type log
        	:arg group (string): Groupname to belongs the file type log
		"""
		logger = getLogger(name_log)
		logger.setLevel(INFO)
		if (logger.hasHandlers()):
   	 		logger.handlers.clear()
		if "use_stream_handler" in kwargs and kwargs["use_stream_handler"] == True:
			sh = StreamHandler()
			formatter_stream_handler = Formatter('%(levelname)s - %(name)s - %(message)s')
			sh.setFormatter(formatter_stream_handler)
			logger.addHandler(sh)
		if "use_file_handler" in kwargs and kwargs["use_file_handler"] == True:
			path_log_file = kwargs["name_file_log"] + str(date.today()) + ".log"
			fh = FileHandler(path_log_file)
			formatter_file_handler = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
			fh.setFormatter(formatter_file_handler)
			logger.addHandler(fh)
			if "user" in kwargs and "group" in kwargs:
				self.__utils.changeOwnerToPath(path_log_file, kwargs["user"], kwargs["group"])
		if log_level == 1:
			logger.info(message)
		elif log_level == 2:
			logger.warning(message)
		elif log_level == 3:
			logger.error(message)