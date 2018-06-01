import sys
import os

class FileLogger(object):
    def __init__(self, filename, mode="a"):
        self.stdout = sys.stdout
        self.file = open(filename, mode)
        sys.stdout = self

    def __del__(self):
        self.close()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.close()

    def write(self, message):
        self.stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.stdout.flush()
        self.file.flush()
        os.fsync(self.file.fileno())

    def close(self):
        if self.stdout:
            sys.stdout = self.stdout
            self.stdout = None

if __name__ == "__main__":
    with FileLogger('test.log', 'a'):
        print 'logger test'
