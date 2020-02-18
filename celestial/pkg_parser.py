#!/usr/bin/env python3
import json
import pathlib
from os import chdir, chmod

class Parser:
    def __init__(self, pkg_template):
        self.template_dict = self.__parse(pkg_template)
        self.template_path = self.__get_pkg_template_abs_path(pkg_template)

        chdir(self.template_path)
    
    def __get_pkg_template_abs_path(self, pkg_template):
        if not pathlib.Path.exists(pathlib.Path(pkg_template)):
            raise FileNotFoundError

        return pathlib.Path(pkg_template).absolute().resolve()

    def __parse(self, pkg_template):
        try:
            return json.loads(self.get_pkg_template_abs_path(pkg_template))
        except:
            raise

    def get_deps(self):
        return self.template_dict["dependencies"]

    def get_metadata(self):
        metadata = {"name": self.template_dict["name"],
                    "version": self.template_dict["version"],
                    "description": self.template_dict["description"],
                    "maintainer": self.template_dict["maintainer"]
                   }
        return metadata

    def generate_build_script(self):
        build_script = open("build.sh", "w")
        build_script.write("#!/usr/bin/bash\n")

        for i in self.template_dict["build"]:
            build_script.write(f"{i}\n")
        build_script.close()
        chmod(pathlib.Path(build_script).absolute().resolve(), 0o755)