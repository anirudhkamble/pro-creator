#!/usr/bin/env python
import os

import click

from creator.managers import Manager as _Manager


def create_project_path(name, basepath=None):
    if basepath is not None:
        return os.path.join(basepath, name)
    else:
        return os.path.join(name)


def create_path_list(root, children=[]):

    paths = [root]
    for child in children:
        if child is not None:
            paths.append(os.path.join(root, child))

    return paths


@click.group()
def project():
    pass


@project.command()
@click.argument("name")
@click.option("--source")
@click.option("--tests")
@click.option("--resources")
@click.option("--basepath")
def create(name, source=None, tests=None, resources=None, basepath=None):
    project_path = create_project_path(name, basepath)
    paths = create_path_list(project_path, [source, tests, resources])
    managerClass = _Manager(name, project_path, paths)
    managerClass.init_project()
    managerClass.show()


@project.command()
@click.argument("name")
@click.option("--basepath")
def destroy(name, basepath=None):
    project_path = create_project_path(name, basepath)
    managerClass = _Manager(name, project_path)
    managerClass.destroy_project()


if __name__ == "__main__":
    project()
