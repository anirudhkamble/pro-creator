import os as _os
import shutil as _shutil
import unittest as _unittest
from unittest import TestCase

from creator.managers import DirectoryManager, FileManager, Manager


CWD = _os.path.abspath("./tests")


class TestBase(TestCase):

    def setUp(self):
        test_dir = "test_dir"
        self.paths = [
            "%s/%s" % (CWD, test_dir),
            "%s/%s/%s" % (CWD, test_dir, self.name + "1"),
            "%s/%s/%s" % (CWD, test_dir, self.name + "2")
        ]

    def tearDown(self):
        try:
            _shutil.rmtree(self.paths[0])
        except FileNotFoundError:
            pass


class Test_DirectoryManager(TestBase):

    def setUp(self):
        self.name = "dir"
        super(Test_DirectoryManager, self).setUp()

        self.dm = DirectoryManager(self.paths)

    def test_mk_dirs(self):
        self.dm.mk_dirs()
        for path in self.paths:
            self.assertTrue(_os.path.exists(path))

    def test_rm_dirs(self):
        self.dm.mk_dirs()
        for path in self.paths:
            self.assertTrue(_os.path.exists(path))

        self.dm.rm_dirs(self.paths)
        for path in self.paths:
            self.assertFalse(_os.path.exists(path))


if __name__ == "__main__":
    _unittest.main()
