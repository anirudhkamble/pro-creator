import os as _os
import pathlib as _pathlib
import shutil as _shutil


def pathKlass(path):
    return _pathlib.Path(path)


class DirectoryManager(object):

    def __init__(self, paths=[]):
        super(DirectoryManager, self).__init__()

    def mkdirs(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.exists():
                path.mkdir()

    def rmdirs(self, paths=[]):
        for path in paths:
            path = pathKlass(path)
            if path.exists():
                path.rmdir()


class FileManager(object):

    def __init__(self, paths=[]):
        super(FileManager, self).__init__()

    def mkfile(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.parent.exists():
                path.parent.mkdir()
            open(str(path), "wb")

    def rmfiles(self):
        for path in self.paths:
            path = pathKlass(path)
            if path.parent.exists() and path.is_file():
                _os.remove(str(path))

    def mkinits(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.parent.exists():
                path.parent.mkdir()
            open("%s/__init__.py" % path, "wb")

    def mkmake(self):
        open("%s/Makefile" % self.project_path, "wb")

    def mksetup(self):
        open("%s/setup.py" % self.project_path, "wb")


class Manager(DirectoryManager, FileManager):

    def __init__(self, name, project_path, paths=[]):
        super(Manager, self).__init__()
        self.name = name
        self.project_path = project_path
        self.paths = paths

    def init_project(self):
        self.mkdirs()
        self.mkinits()
        self.mksetup()
        self.mkmake()

    def destroy_project(self):
        print(
            "Deleting project `%s` from location `%s` ...."
            % (self.name, self.project_path)
        )
        _shutil.rmtree(self.project_path)
        print("Deleted")

    def show(self):
        print("#" * 120)
        print(
            "##### Project `%s` created at location `%s` " 
            % (self.name, self.project_path)
        )
        _os.system("tree %s" % self.project_path)
