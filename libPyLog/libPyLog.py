"""
Author: Erick Roberto Rodriguez Rodriguez
Email: erodriguez@tekium.mx, erickrr.tbd93@gmail.com
GitHub: https://github.com/erickrr-bd/libPyLog
libPyLog v2.2 - March 2025
"""
from datetime import date
from dataclasses import dataclass
from libPyUtils import libPyUtils
from logging import getLogger, INFO, Formatter, FileHandler, StreamHandler

@dataclass
class libPyLog:
	"""
	Easy writing of application logs with Python.
	"""

	def create_log(self, message: str, level: int, name: str, **kwargs) -> None:
		"""
		Method that creates application logs (stream and file).

		Parameters:
			message (str): Message to display in the log.
			level (int): Level or criticality of the log.
			name (str): Log name.
		
		Keyword Args:
			use_stream_handler (bool): Option to create a log that is only displayed on the screen.
			use_file_handler (bool): Option to create a log file.
			file_name (str): Log file.
			user (str): Owner user.
			group (str): Group owner.
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
				utils = libPyUtils()
				utils.change_owner(log_file, kwargs["user"], kwargs["group"], "644")
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