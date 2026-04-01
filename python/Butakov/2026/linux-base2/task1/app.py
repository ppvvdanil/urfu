from typing import List
import os
import signal
import subprocess

from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    if not isinstance(port, int):
        raise ValueError

    result = subprocess.run(
        ["lsof", "-t", f"-i:{port}"],
        capture_output=True,
        text=True,
        check=False,
    )

    pids: List[int] = []
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.isdigit():
            pids.append(int(line))

    return pids


def free_port(port: int) -> None:
    pids: List[int] = get_pids(port)
    for pid in pids:
        os.kill(pid, signal.SIGTERM)


def run(port: int) -> None:
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)
