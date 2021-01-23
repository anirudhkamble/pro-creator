#!/usr/bin/env python
import os

import click

from creator.managers import Manager as _Manager


def create_project_path(name, location=None):
    if location is not None:
        return os.path.join(location, name)
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
@click.argument("name", "Name of the project.")
@click.option("--source", "-s", help="Name for the source directory.")
@click.option("--tests", "-t", help="Name for the testcase directory.")
@click.option("--resources", "-r", help="Name for the resources directory.")
@click.option("--location", "-l", help="Parent directory location of the project.")
def create(name, source=None, tests=None, resources=None, location=None):
    project_path = create_project_path(name, location)
    paths = create_path_list(project_path, [source, tests, resources])
    managerClass = _Manager(name, project_path, paths)
    managerClass.init_project()
    managerClass.show()


@project.command()
@click.argument("name", "Name of the project.")
@click.option("--location", "-l", help="Parent directory location of the project.")
def destroy(name, location=None):
    project_path = create_project_path(name, location)
    managerClass = _Manager(name, project_path)
    managerClass.destroy_project()


if __name__ == "__main__":
    project()
