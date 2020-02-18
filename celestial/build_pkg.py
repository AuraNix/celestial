#!/usr/bin/env python3

#Our imports
import celestial.pkg_parser as parser
import celestial.dep_resol as dep_resolver

#General imports
import pathlib
import subprocess

def build_pkg(pkg_template):
    pkg_parser = parser.Parser(pkg_template)

    dependencies = pkg_parser.get_deps()
    metadata = pkg_parser.get_metadata()

    pkg_parser.generate_build_script()
    dep_resolver.install_dependencies(pkg_parser.get_deps())


def catalogue_pkg(metadata):
    #Probably use an sqlite database to keep track of packages
    pass