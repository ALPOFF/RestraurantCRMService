from dev.configuration_loader import load_configuration
from v1.api import get_api_v1
from fastapi.middleware.cors import CORSMiddleware

load_configuration()

# Delete in production
origins = [
    "*"
]

application = get_api_v1()
application.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                           allow_headers=["*"])

