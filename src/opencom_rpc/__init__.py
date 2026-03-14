"""Helpers for interacting with the OpenCom RPC server."""

from .client import DEFAULT_BASE_URL, DEFAULT_MEDIA_POLL_SECONDS, OpenComRPCClient
from .models import Activity, ActivityButton

__version__ = "0.1.0"

__all__ = [
    "Activity",
    "ActivityButton",
    "DEFAULT_BASE_URL",
    "DEFAULT_MEDIA_POLL_SECONDS",
    "OpenComRPCClient",
    "__version__",
]
