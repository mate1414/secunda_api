from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.core.config import settings


API_KEY_NAME = "X-API-Key"


async def auth_middleware(request: Request, call_next):
    if request.url.path in ["/docs", "/redoc", "/openapi.json", "/health"]:
        return await call_next(request)

    api_key = request.headers.get(API_KEY_NAME)

    if not api_key:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Missing API key"}
        )

    if api_key != settings.STATIC_API_KEY:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Invalid API key"}
        )

    response = await call_next(request)
    return response


def add_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def _auth_middleware(request: Request, call_next):
        await auth_middleware(request=request, call_next=call_next)
