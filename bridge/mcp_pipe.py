#!/usr/bin/env python3
"""
Public reference bridge for Xiaozhi -> n8n.

Input:
    One JSON object per line on stdin.

Output:
    A compact JSON result per line on stdout.

This intentionally contains no credentials.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request


WEBHOOK_URL = os.getenv(
    "N8N_WEBHOOK_URL",
    "http://127.0.0.1:5678/webhook-test/xiaozhi",
)
SHARED_SECRET = os.getenv("BRIDGE_SHARED_SECRET", "")


def post_to_n8n(payload: dict) -> tuple[int, str]:
    body = json.dumps(payload).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "xiaozhi-n8n-public-bridge/1.0",
    }

    if SHARED_SECRET:
        headers["X-Bridge-Secret"] = SHARED_SECRET

    request = urllib.request.Request(
        WEBHOOK_URL,
        data=body,
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            text = response.read().decode("utf-8", errors="replace")
            return response.status, text
    except urllib.error.HTTPError as exc:
        text = exc.read().decode("utf-8", errors="replace")
        return exc.code, text


def handle_line(line: str) -> dict:
    try:
        payload = json.loads(line)
    except json.JSONDecodeError as exc:
        return {
            "ok": False,
            "error": "invalid_json",
            "detail": str(exc),
        }

    if not isinstance(payload, dict):
        return {
            "ok": False,
            "error": "payload_must_be_json_object",
        }

    try:
        status, response_text = post_to_n8n(payload)
        return {
            "ok": 200 <= status < 300,
            "status": status,
            "response": response_text[:1000],
        }
    except Exception as exc:
        return {
            "ok": False,
            "error": type(exc).__name__,
            "detail": str(exc),
        }


def main() -> int:
    for raw_line in sys.stdin:
        line = raw_line.strip()
        if not line:
            continue

        result = handle_line(line)
        print(json.dumps(result), flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
