#!/usr/bin/env python3

#Our imports
import celestial.pkg_parser as parser
import celestial.dep_resol as dep_resolver

#General imports
import pathlib
import subprocess

def build_pkg(pkg_template):
    pkg_parser = parser.Parse(pkg_template)
    metadata = pkg_parser.get_metadata()

    pkg_parser.generate_build_script()

    dep_resolver.install_dependencies(metadata["dependencies"])

    try:
        subprocess.run(["build.sh"], check=True)
        catalogue_pkg(metadata)
    except subprocess.CalledProcessError:
        print("Failed to build package. See build log for details.")

def catalogue_pkg(metadata):
    #Probably use an sqlite database to keep track of packages
    pass