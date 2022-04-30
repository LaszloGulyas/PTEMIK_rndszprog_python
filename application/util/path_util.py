from pathlib import Path


class PathUtil:
    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent.parent

    @staticmethod
    def get_project_resources() -> Path:
        return PathUtil.get_project_root().joinpath("resources")
