"""
Author: Erick Roberto Rodriguez Rodriguez
Email: erodriguez@tekium.mx, erickrr.tbd93@gmail.com
GitHub: https://github.com/erickrr-bd/libPyLog
libPyLog v2.2.1 - July 2026
Dynamic and secure wrapper built on top of Python's native logging library.
"""
from datetime import date
from libPyUtils import libPyUtils
from logging import getLogger, DEBUG, INFO, WARNING, ERROR, CRITICAL, Formatter, FileHandler, StreamHandler

class libPyLog:

	def create_log(self, message: str, level: int, name: str, **kwargs) -> None:
		"""
		Method that creates application logs (stream and file).

		Parameters:
			message (str): The text message or exception object to register.
			level (int): Logging severity represented as an integer.
			name (str): The unique identifier/logger channel name.
		
		Keyword Args:
			use_stream_handler (bool): If True, enables clean stdout logging format to the terminal.
			use_file_handler (bool): If True, enables writing logs to disk. (Requires file_name).
			file_name (str): Base file path/prefix where the date-bound file will be created.
			user (str): The target UNIX user who will own the file.
			group (str): The target UNIX group who will own the file.
		"""
		logger = getLogger(name)
		logger.setLevel(DEBUG)
		file_handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		stream_handler_format = Formatter('%(levelname)s - %(name)s - %(message)s')
		if kwargs.get("use_stream_handler"):
			has_stream = any(isinstance(h, StreamHandler) and not isinstance(h, FileHandler) for h in logger.handlers)
			if not has_stream:
				stream_handler = StreamHandler()
				stream_handler.setFormatter(stream_handler_format)
				logger.addHandler(stream_handler)
		if kwargs.get("use_file_handler") and "file_name" in kwargs:
			log_file = f"{kwargs["file_name"]}-{date.today()}.log"
			has_file_handler = any(isinstance(h, FileHandler) and h.baseFilename.endswith(log_file) for h in logger.handlers)
			if not has_file_handler:
				for h in list(logger.handlers):
					if isinstance(h, FileHandler):
						h.close()
						logger.removeHandler(h)
				file_handler = FileHandler(log_file)
				file_handler.setFormatter(file_handler_format)
				logger.addHandler(file_handler)
				if "user" in kwargs and "group" in kwargs:
					try:
						utils = libPyUtils()
						utils.change_owner(log_file, kwargs["user"], kwargs["group"], "640")
					except Exception:
						pass
		str_message = str(message)
		match level:
			case 1:
				logger.debug(str_message)
			case 2:
				logger.info(str_message)
			case 3:
				logger.warning(str_message)
			case 4:
				logger.error(str_message)
			case 5:
				logger.critical(str_message)
