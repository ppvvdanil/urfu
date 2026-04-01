from types import TracebackType
from typing import Type, Literal, IO
import sys
import traceback


class Redirect:
    def __init__(self, *, stdout: IO | None = None, stderr: IO | None = None) -> None:
        self._stdout = stdout
        self._stderr = stderr
        self._old_stdout: IO | None = None
        self._old_stderr: IO | None = None

    def __enter__(self):
        self._old_stdout = sys.stdout
        self._old_stderr = sys.stderr
        if self._stdout is not None:
            sys.stdout = self._stdout
        if self._stderr is not None:
            sys.stderr = self._stderr
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, exc_tb, file=sys.stderr)

        if self._old_stdout is not None:
            sys.stdout = self._old_stdout
        if self._old_stderr is not None:
            sys.stderr = self._old_stderr

        if exc_type is not None:
            return True
        return None
