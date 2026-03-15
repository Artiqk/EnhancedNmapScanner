import logging

class ColorFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG:    "\033[3;32m",   # italic green
        logging.INFO:     "\033[0m",      # default
        logging.WARNING:  "\033[33m",     # yellow
        logging.ERROR:    "\033[31m",     # red
        logging.CRITICAL: "\033[1;31m",   # bold red
    }

    RESET = "\033[0m"
    BASE_FMT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FMT = "%Y-%m-%d %H:%M:%S"

    def format(self, record):
        color = self.FORMATS.get(record.levelno, self.RESET)
        formatter = logging.Formatter(
            fmt=f"{color}{self.BASE_FMT}{self.RESET}",
            datefmt=self.DATE_FMT
        )
        return formatter.format(record)