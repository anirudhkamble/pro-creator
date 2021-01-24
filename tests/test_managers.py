import os as _os
import shutil as _shutil
import unittest as _unittest
from unittest import TestCase

from creator.managers import DirectoryManager, FileManager, Manager


CWD = _os.path.abspath("./tests")


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
            _shutil.rmtree(self.paths[0])
        except FileNotFoundError:
            pass

    def test_mk_dirs(self):
        self.dm.mk_dirs()
        for path in self.paths:
            self.assertTrue(_os.path.exists(path))

    def test_rm_dirs(self):
        self.dm.mk_dirs()
        for path in self.paths:
            self.assertTrue(_os.path.exists(path))

        self.dm.rm_dirs(self.paths)


if __name__ == "__main__":
    _unittest.main()
