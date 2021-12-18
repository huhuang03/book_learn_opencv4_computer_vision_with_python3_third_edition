import os


def img_path(name: str) -> str:
    return os.path.join(__path__[0], name)
