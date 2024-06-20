"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .builtins import *
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)

def get_alerts(config, params):
    try:
      QUERY = "$expand=TriggeringEvents,Source&$top=" + str(params.get("limit")) + "&$filter=CreationTimestamp gt " + str(params.get("startTime")) + " and CreationTimestamp lt " + str(params.get("endTime"))
      response = api_query_call(config, query=QUERY)
      if response.status_code != requests.codes.ok:
        logger.info(f"Error {response.status_code} - {response.text}")
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)