from typing import Any
from .bus import event_bus


class BaseService:
    def publish_event(self, event: str, **payload: Any) -> None:
        event_bus.publish(event, **payload)
