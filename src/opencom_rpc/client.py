from __future__ import annotations

from typing import Any, Mapping

import requests

from .models import Activity

DEFAULT_BASE_URL = "http://127.0.0.1:6483"
DEFAULT_MEDIA_POLL_SECONDS = 3.0


class OpenComRPCClient:
    """Small requests-based client for the OpenCom RPC server."""

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        *,
        timeout: float = 5.0,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()
        self._owns_session = session is None

    def build_url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def request(
        self,
        method: str,
        path: str,
        *,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> requests.Response:
        response = self.session.request(
            method=method.upper(),
            url=self.build_url(path),
            timeout=self.timeout if timeout is None else timeout,
            **kwargs,
        )
        response.raise_for_status()
        return response

    def request_json(
        self,
        method: str,
        path: str,
        *,
        timeout: float | None = None,
        **kwargs: Any,
    ) -> Any:
        response = self.request(method, path, timeout=timeout, **kwargs)
        if not response.content:
            return None
        return response.json()

    def health(self) -> Any:
        return self.request_json("GET", "/rpc/health", timeout=3)

    def set_activity(self, activity: Activity | Mapping[str, Any]) -> Any:
        if isinstance(activity, Activity):
            payload = {"activity": activity.to_dict()}
        else:
            raw_activity = dict(activity)
            payload = raw_activity if "activity" in raw_activity else {"activity": raw_activity}

        return self.request_json("POST", "/rpc/activity", json=payload)

    def clear_activity(self) -> None:
        self.request("DELETE", "/rpc/activity", timeout=3)

    def close(self) -> None:
        if self._owns_session:
            self.session.close()

    def __enter__(self) -> OpenComRPCClient:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()
