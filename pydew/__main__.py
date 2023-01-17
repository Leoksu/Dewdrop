from logging import getLogger, basicConfig
from pyrogram import idle, Client
from pathlib import Path
from . import *
from .configs import *
from .stuff.utils import load_plugins
import asyncio
import glob

logger = getLogger("DewLogs")

async def main():
    ghoul = Client(
                ".dew",
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=BOT_TOKEN,
                plugins=dict(root="pydew/modules")
            )
    logger.info("Importing Modules")
    logger.info(
        """
               --------------------------------------------------------------------------------------
                             Your bot has been started, see @TheGhostOrg for updates
               --------------------------------------------------------------------------------------
    """
    )
    await ghoul.start()
    await idle()

loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(main())
    logger.info(" --- Bot has been stopped ---")
