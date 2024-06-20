"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import requests
import base64
from .constants import REQUEST_TIMEOUT, LOGGER_NAME, AUTH_API_ENDPOINT, ALERTS_API_ENDPOINT
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger(LOGGER_NAME)

def get_auth_token(config, **kwargs):
    try:
        url = config.get("authenticationURL") + AUTH_API_ENDPOINT
        auth_header = {
            'Authorization': 'Basic ' + base64.b64encode(( config.get("clientID") + ':' + config.get("clientSecret")).encode()).decode()
        }
        response = requests.post(url=url, headers=auth_header, timeout=REQUEST_TIMEOUT)
        if response.status_code != requests.codes.ok:
            logger.error("Error: {0}".format(response.content))
            raise ConnectorError('Error: {0}'.format(response.content))
        TOKEN = response.json()['access_token']
        if not TOKEN:
            logger.error("Error: {0}".format(response_json.get("message")))
            raise Exception('Error: {0}'.format(response_json.get("message")))
        return TOKEN
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))

def api_query_call(config, query=None, **kwargs):
    try:
        url = config.get("eTDDataRetrievalURL") + ALERTS_API_ENDPOINT
        TOKEN = get_auth_token(config)
        HEADERS = { 'Authorization': 'Bearer ' + TOKEN}
        result = requests.get(url=url + query, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        return result
    except Exception as e:
        logger.error('{0}'.format(e))
        raise ConnectorError('{0}'.format(e))