import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
import logging.config
import yaml
from utils.config import Config
from configs.config import CFG

config = Config.from_json(CFG)

with open(config.project.path + '/src/configs/logging_config.yaml', 'r') as f:
    config_log = yaml.safe_load(f.read())
    logging.config.dictConfig(config_log)
    logging.captureWarnings(True)

def get_logger(name: str):
    """Logs a message
    Args:
    name(str): name of logger
    """
    logger = logging.getLogger(name)
    return logger
