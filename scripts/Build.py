from subprocess import check_call
from os import path

class Build:
    def __init__(self, verbose):
        self._build_dir = 'build'
        self._generator = 'Ninja'
        self._extra_gen_args = []
        self._extra_build_args = []
        self._verbose = verbose
        self._tests_target = 'test'

    def build_dir(self):
        return self._build_dir

    def generate(self):
        args = ['cmake', '-S', '.', '-B', self._build_dir, '-G', self._generator]
        args.extend(self._extra_gen_args)
        self._execute(args)

    def make(self):
        if not path.exists(self._build_dir):
            self.generate()

        args = ['cmake', '--build', self._build_dir]
        args.extend(self._extra_build_args)
        if self._verbose:
            args.append('-v')

        self._execute(args)

    def test(self):
        args = ['cmake', '--build', self._build_dir]
        args.extend(self._extra_build_args)
        args.extend(['--target', self._tests_target])

        self._execute(args)

    def clean(self):
        args = ['cmake', '--build', self._build_dir]
        args.extend(self._extra_build_args)
        args.extend(['--target', 'clean'])

        self._execute(args)

    def _execute(self, args):
        check_call(args)

class SingleConfigBuild(Build):
    def __init__(self, build_type, verbose):
        super(SingleConfigBuild, self).__init__(verbose)

        self._build_dir = str(path.join('build', build_type.lower()))
        self._extra_gen_args += [f'-DCMAKE_BUILD_TYPE={build_type}']

class MultiConfigBuild(Build):
    def __init__(self, build_type, verbose):
        super(MultiConfigBuild, self).__init__(verbose)

        self._extra_build_args = ['--config', build_type]

class WindowsBuild(MultiConfigBuild):
    def __init__(self, build_type, verbose):
        super(WindowsBuild, self).__init__(build_type, verbose)
        self._generator = 'Visual Studio 16 2019'
        self._tests_target = 'RUN_TESTS'
        self._extra_gen_args += ['-A', 'x64']

class LinuxBuild(SingleConfigBuild):
    def __init__(self, build_type, verbose):
        super(LinuxBuild, self).__init__(build_type, verbose)
        self._extra_gen_args += ['-DCMAKE_C_COMPILER=clang',
                                 '-DCMAKE_CXX_COMPILER=clang++']
