import sys
sys.argv = [sys.argv[0], "build_ext", "--inplace"]

from setuptools import Extension, setup
from Cython.Build import cythonize
import os
import platform


libraries = {
    "Darwin": [
        "glad",
        "glfw"
    ]
}
include_dirs = [
    "./engine/libs/include", 
    "./engine/libs"
]
library_dirs = {
    "Darwin": ["./engine/libs/shared/Darwin"],
}

language = "c++"
default = ["-w"]
debug_args = ["-w", "-std=c11", "-O0"]
release_args = ["-w", "-std=c11", "-O3", "-ffast-math", "-march=native"]

args = default
# args = debug_args
# args = release_args

annotate = False
force = False

if __name__ == "__main__":
    system = platform.system()
    
    libs = libraries[system]
    lib_dirs = library_dirs[system]
    extensions = []

    # for path, dirs, file_names in os.walk("."):
    #     for file_name in file_names:
    #         if file_name.endswith("pyx"):
    #             ext_path = "{0}/{1}".format(path, file_name)
    #             ext_name = (
    #                 ext_path
    #                 .replace("./", "")
    #                 .replace("/", ".")
    #                 .replace(".pyx", "")
    #             )
    #             ext = Extension(
    #                 name=ext_name, 
    #                 sources=[ext_path], 
    #                 libraries=libs,
    #                 language=language,
    #                 include_dirs=include_dirs,
    #                 library_dirs=lib_dirs,
    #                 runtime_library_dirs=lib_dirs,
    #                 extra_compile_args=args,
    #             )
    #             extensions.append(ext)

    files= [
        ("engine.render", "./engine/render.pyx"),
        ("engine.window", "./engine/window.pyx"),
        ("engine.constants", "./engine/constants.py")
    ]
    for ext_name, ext_path in files:
        ext = Extension(
            name=ext_name, 
            sources=[ext_path], 
            libraries=libs,
            language=language,
            include_dirs=include_dirs,
            library_dirs=lib_dirs,
            runtime_library_dirs=lib_dirs,
            extra_compile_args=args,
        )
        extensions.append(ext)


    setup(
        ext_modules=cythonize(
            module_list=extensions, 
            annotate=annotate,
            compiler_directives={'language_level' : "3"},
            force=force
        ),
    )

# export DYLD_FALLBACK_LIBRARY_PATH=/Users/williamhou/Documents/Coding/Personal-coding/2D-Graphics-Lib/engine/libs/shared/Darwin
