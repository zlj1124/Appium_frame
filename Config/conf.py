'''
@Descripttion: 
@Author: zlj
@Date: 2020-06-03 15:47:09
'''
import os
import logging

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF_PATH = os.path.join(ROOT_DIR, 'Config', 'location.ini')
DATA_Path = os.path.join(ROOT_DIR,'data','tcData.xlsx')

LOG_CONFIG_LOCATION = 'Config/logging_config.ini'
LOG_LEVEL = logging.DEBUG