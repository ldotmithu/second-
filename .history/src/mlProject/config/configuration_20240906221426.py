from mlProject.utils.common import *
from mlProject.constants import *

class ConfigurationManager:
    def __init__(self):
        config=read_yaml(CONFIG_FILE_PATH)
        