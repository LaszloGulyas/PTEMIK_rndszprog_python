import unittest

from application.util.path_util import PathUtil


class TestPathUtil(unittest.TestCase):
    def test_project_root_exists(self):
        root_path = PathUtil.get_project_root()
        self.assertTrue(root_path.exists())

    def test_resources_folder_exists(self):
        resources_path = PathUtil.get_project_resources()
        self.assertTrue(resources_path.exists())
