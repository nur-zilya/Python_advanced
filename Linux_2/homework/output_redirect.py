import sys

class Redirect:
    def __init__(self, *, stdout=None, stderr=None):
        self._stdout = stdout
        self._stderr = stderr

    def __enter__(self):
        self._old_stdout = sys.stdout
        self._old_stderr = sys.stderr
        if self._stdout:
            sys.stdout = self._stdout
        if self._stderr:
            sys.stderr = self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        if self._stdout:
            sys.stdout.flush()
            sys.stdout = self._old_stdout
        if self._stderr:
            sys.stderr.flush()
            sys.stderr = self._old_stderr
        return False
