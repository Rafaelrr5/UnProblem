from enum import auto
import sys
import os
from typing import Optional
from cx_Freeze import *

files=["ui_main.py","ui_splash_screen.py"]

target = Executable(
    script="main.py",
    base="Win32GUI"
)

setup(
    name = "UnProblem",
    version = "2.0",
    description = "",
    author = "Rafael Rocha Ribeiro",
    options = {'build.exe' : {'include_files' : files}},
    executables = [target]
)