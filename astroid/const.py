import enum
import sys

__all__ = ["Load", "Store", "Del", "Context"]

PY37 = sys.version_info >= (3, 7)
PY38 = sys.version_info >= (3, 8)
PY39 = sys.version_info >= (3, 9)
PY310 = sys.version_info >= (3, 10)


class Context(enum.Enum):
    Load = 1
    Store = 2
    Del = 3


Load = Context.Load
Store = Context.Store
Del = Context.Del