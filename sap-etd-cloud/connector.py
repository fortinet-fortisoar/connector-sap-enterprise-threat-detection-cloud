"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
from connectors.core.connector import Connector
from connectors.core.connector import get_logger, ConnectorError
from django.utils.module_loading import import_string
from .builtins import *
from .constants import LOGGER_NAME
from .utils import api_query_call

logger = get_logger(LOGGER_NAME)


class Sap_etd_cloud(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        return supported_operations.get(operation)(config, params)

    def check_health(self, config, *args, **kwargs):
        try:
            response = api_query_call(config, query="$top=1")
            if response.ok:
                logger.info("Connector is available")
                return True
            else:
                raise ConnectorError(f"Error {response.status_code} - {response.text}")
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)