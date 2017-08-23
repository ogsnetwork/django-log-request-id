import threading


__version__ = "1.5"


local = threading.local()

REQUEST_ID_IGNORE_PATHS = 'REQUEST_ID_IGNORE_PATHS'
REQUEST_ID_HEADER_SETTING = 'LOG_REQUEST_ID_HEADER'
LOG_REQUESTS_SETTING = 'LOG_REQUESTS'
NO_REQUEST_ID = "none"  # Used if no request ID is available
REQUEST_ID_RESPONSE_HEADER_SETTING = 'REQUEST_ID_RESPONSE_HEADER'
OUTGOING_REQUEST_ID_HEADER_SETTING = 'OUTGOING_REQUEST_ID_HEADER'
GENERATE_REQUEST_ID_IF_NOT_IN_HEADER_SETTING = 'GENERATE_REQUEST_ID_IF_NOT_IN_HEADER'
