import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .builtins import *
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_alert_by_id(config, params):
    try:
      QUERY = "$expand=Source,TriggeringEvents&$filter=AlertId eq " + str(params.get("alertID"))
      response = api_query_call(config, query=QUERY)
      if response.status_code != requests.codes.ok:
        logger.info(f"Error {response.status_code} - {response.text}")
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)