import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .builtins import *
from .utils import api_query_call
logger = get_logger(LOGGER_NAME)


def get_investigations(config, params):
    try:
      QUERY = "$expand=Investigations&$filter=Investigations/any(a:a/Id eq "+ str(params.get("alertID")) + ")&$top=" + str(params.get("limit"))
      response = api_query_call(config, query=QUERY)
      if response.status_code != requests.codes.ok:
        logger.info(f"Error {response.status_code} - {response.text}")
      return response.json()
    except Exception as err:
      logger.exception(err)
      raise ConnectorError(err)