import os
import shutil
import unittest
from unittest import TestCase

from creator.managers import DirectoryManager, FileManager, Manager


CWD = os.path.abspath("./tests")


class Test_DirectoryManager(TestCase):

    def setUp(self):
        self.paths = [
            "%s/%s" % (CWD, "test_dir"),
            "%s/%s/%s" % (CWD, "test_dir", "dir1"),
            "%s/%s/%s" % (CWD, "test_dir", "dir2")
        ]
        self.dm = DirectoryManager(self.paths)

    def tearDown(self):
        try:
            shutil.rmtree(self.paths[0])
        except FileNotFoundError:
            pass

    def test_mkdirs(self):
        self.dm.mkdirs()
        for path in self.paths:
            self.assertTrue(os.path.exists(path))


if __name__ == "__main__":
    unittest.main()
