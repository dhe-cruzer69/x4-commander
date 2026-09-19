"""Structural orchestrator scaffold. No production claims at L0."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Commander:
    name: str = "x4-commander"
    version: str = "0.0.1"
    tasks: list[dict[str, Any]] = field(default_factory=list)

    def enqueue(self, task: dict[str, Any]) -> str:
        if not isinstance(task, dict) or "id" not in task:
            raise ValueError("task must be a dict with an id")
        self.tasks.append(task)
        return str(task["id"])

    def health(self) -> dict[str, str]:
        return {"status": "ok", "server": self.name, "version": self.version}
