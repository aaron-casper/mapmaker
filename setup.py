from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('.\\mapmaker.py', base=base, targetName = '.\\mapmaker.exe')
]

setup(name='mapmaker',
      version = '0.0.3',
      description = 'besiege map prefab tool',
      options = dict(build_exe = buildOptions),
      executables = executables)
