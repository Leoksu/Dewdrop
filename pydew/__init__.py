import sys
import os
import platform
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from pyrogram import Client
from .configs import *


dewlog = f"dews{sys.argv[6]}.log" if len(sys.argv) > 6 else "dews.log"
logger = getLogger("DewLogs")
if os.path.exists(dewlog):
    os.remove(dewlog)

_LOG_FORMAT = "%(asctime)s | %(name)s [%(levelname)s] : %(message)s"
basicConfig(
    format=_LOG_FORMAT,
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
    handlers=[FileHandler(dewlog), StreamHandler()],
)

logger.info("[---------->>> Starting your deployement <<<----------]")
logger.info(f"Deploying with python-{platform.python_version()}")
logger.info("Initializing...")
if not os.path.exists("pydew/modules"):
    logger.error(
        "Can't fine 'modules' folder\nMake sure that, you are on correct path."
    )
    logger.info("Exiting...")
    exit()

