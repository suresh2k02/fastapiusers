from fastapi import FastAPI
from app.routes.user import user
from app.config.tags import tags_metadata
from app.config.description import description

app = FastAPI(
    title="REST API Users",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata,
    terms_of_service="http://example.com/terms/",
    contact={
        "name": " ",
        "url": "https://medium.com/",
        "email": "user@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(user)
