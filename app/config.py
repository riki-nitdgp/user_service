from app.utils.common_utils import json_file_to_dict
import os


class AppConfig:
    config = json_file_to_dict(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json'))

