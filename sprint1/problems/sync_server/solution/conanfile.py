import os
from conan import ConanFile
from conan.tools.cmake import cmake_layout


class ExampleRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("boost/1.86.0")

    def layout(self):
        # cmake_layout(self)
        self.folders.generators = os.path.join("build", "generators")
        self.folders.build = os.path.join("build")