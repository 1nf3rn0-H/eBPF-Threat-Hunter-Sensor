#!/usr/bin/env python3
"""Compatibility wrapper for the packaged Kernel Flight Recorder."""

from kernel_flight_recorder.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
