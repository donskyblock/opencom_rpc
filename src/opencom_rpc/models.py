from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ActivityButton:
    """Clickable button shown in the OpenCom activity payload."""

    label: str
    url: str

    def to_dict(self) -> dict[str, str]:
        return {
            "label": self.label,
            "url": self.url,
        }


@dataclass(slots=True)
class Activity:
    """Structured representation of an OpenCom activity."""

    name: str
    details: str | None = None
    state: str | None = None
    start_timestamp: int | None = None
    end_timestamp: int | None = None
    large_image_url: str | None = None
    small_image_url: str | None = None
    buttons: list[ActivityButton] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {"name": self.name}

        if self.details:
            payload["details"] = self.details
        if self.state:
            payload["state"] = self.state
        if self.start_timestamp is not None:
            payload["startTimestamp"] = self.start_timestamp
        if self.end_timestamp is not None:
            payload["endTimestamp"] = self.end_timestamp
        if self.large_image_url:
            payload["largeImageUrl"] = self.large_image_url
        if self.small_image_url:
            payload["smallImageUrl"] = self.small_image_url
        if self.buttons:
            payload["buttons"] = [button.to_dict() for button in self.buttons]

        return payload
