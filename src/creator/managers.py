import os as _os
import pathlib as _pathlib
import shutil as _shutil


def pathKlass(path):
    return _pathlib.Path(path)


def create_file(name):
    open(name, "wb")


class DirectoryManager(object):

    def __init__(self, paths=[]):
        super(DirectoryManager, self).__init__()
        self.paths = paths

    def mk_dirs(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.exists():
                path.mkdir()

    def rm_dirs(self, paths=[]):
        for path in paths:
            path = pathKlass(path)
            if path.exists():
                path.rmdir()


class FileManager(object):

    def __init__(self, paths=[]):
        super(FileManager, self).__init__()
        self.paths = paths

    def mk_file(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.parent.exists():
                path.parent.mkdir()
            create_file(str(path))

    def rm_files(self):
        for path in self.paths:
            path = pathKlass(path)
            if path.parent.exists() and path.is_file():
                _os.remove(str(path))

    def mk_inits(self):
        for path in self.paths:
            path = pathKlass(path)
            if not path.parent.exists():
                path.parent.mkdir()
            create_file("%s/__init__.py" % path)

    def mk_make(self):
        create_file("%s/Makefile" % self.project_path)

    def mk_setup(self):
        create_file("%s/setup.py" % self.project_path)


class Manager(DirectoryManager, FileManager):

    def __init__(self, name, project_path, paths=[]):
        super(Manager, self).__init__(paths=paths)
        self.name = name
        self.project_path = project_path
 
    def init_project(self):
        self.mk_dirs()
        self.mk_inits()
        self.mk_setup()
        self.mk_make()

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
