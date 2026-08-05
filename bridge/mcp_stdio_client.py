#!/usr/bin/env python3
"""
Generic stdio launcher used as a public example.

It starts the command in MCP_COMMAND and transparently relays
stdin -> child stdin and child stdout -> stdout.

Example:
    MCP_COMMAND="python3 -u mcp_pipe.py" python3 mcp_stdio_client.py
"""

from __future__ import annotations

import os
import shlex
import subprocess
import sys
import threading


def copy_stream(source, destination) -> None:
    try:
        for chunk in iter(lambda: source.buffer.read(4096), b""):
            destination.buffer.write(chunk)
            destination.buffer.flush()
    except (BrokenPipeError, ValueError):
        pass


def main() -> int:
    command = os.getenv("MCP_COMMAND", "").strip()

    if not command:
        print(
            "MCP_COMMAND is not configured. "
            "Example: MCP_COMMAND='python3 -u mcp_pipe.py'",
            file=sys.stderr,
        )
        return 2

    process = subprocess.Popen(
        shlex.split(command),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=sys.stderr,
        text=False,
    )

    assert process.stdin is not None
    assert process.stdout is not None

    t_in = threading.Thread(
        target=copy_stream,
        args=(sys.stdin, process.stdin),
        daemon=True,
    )
    t_out = threading.Thread(
        target=copy_stream,
        args=(process.stdout, sys.stdout),
        daemon=True,
    )

    t_in.start()
    t_out.start()

    return process.wait()


if __name__ == "__main__":
    raise SystemExit(main())
