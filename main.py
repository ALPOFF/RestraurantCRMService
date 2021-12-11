from dev.configuration_loader import load_configuration
from v1.api import get_api_v1

load_configuration()
application = get_api_v1()
