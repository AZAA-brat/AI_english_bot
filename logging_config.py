import logging
import sys
from logging import basicConfig

def setup_logger() -> None:
    basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
