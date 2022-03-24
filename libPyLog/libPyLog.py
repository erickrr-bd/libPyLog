from datetime import date
from libPyUtils import libPyUtils
from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler

class libPyLog:
	"""
	Attribute that stores an object of the libPyUtils class.
	"""
	__utils = None

	"""
	Attribute that stores a string to define the absolute path of the log file.
	"""
	__name_file_log = None

	"""
	Attribute that stores the name to be assigned to the log.
	"""
	__name_log = None

	"""
	Attribute that stores the owner user of the log file.
	"""
	__user = None

	"""
	Attribute that stores the owner group of the log file.
	"""
	__group = None


	def __init__(self, name_file_log, name_log, user, group):
		"""
		Method that corresponds to the constructor of the class.

		:arg name_file_log: String to define the absolute path of the log file.
		:arg name_log: Name to be assigned to the log.
		:arg user: Owner user of the log file.
		:arg group: Owner group of the log file.
		"""
		self.__user = user
		self.__group = group
		self.__name_log = name_log
		self.__utils = libPyUtils()
		self.__name_file_log = name_file_log


	def createApplicationLog(self, message, log_level, **kwargs):
		"""
		Method that creates an application log.

		:arg message: Message to be displayed in the log.
		:arg log_level: Severity level of the log.
		:arg use_stream_handler: True if the log will also be displayed on the screen. False otherwise.
		"""
		path_log_file = self.__name_file_log + str(date.today()) + ".log"
		logger = getLogger(self.__name_log)
		logger.setLevel(INFO)
		if (logger.hasHandlers()):
   	 		logger.handlers.clear()
		if 'use_stream_handler' in kwargs and kwargs['use_stream_handler'] == True:
			sh = StreamHandler()
			formatter_stream_handler = Formatter('%(levelname)s - %(message)s')
			sh.setFormatter(formatter_stream_handler)
			logger.addHandler(sh)
		fh = FileHandler(path_log_file)
		formatter_file_handler = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		fh.setFormatter(formatter_file_handler)
		logger.addHandler(fh)
		if log_level == 1:
			logger.info(message)
		elif log_level == 2:
			logger.warning(message)
		elif log_level == 3:
			logger.error(message)
		self.__utils.changeOwnerToPath(path_log_file, self.__user, self.__group)