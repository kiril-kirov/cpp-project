import argparse
import platform
import subprocess
import os

class build:
    def __init__(self, cmd_args):
        self._build_dir = 'build'
        self._generator = 'Ninja'
        self._extra_gen_args = []
        self._extra_build_args = []
        self._verbose = cmd_args.verbose
        self._tests_target = 'test'

    def generate(self):
        args = ['cmake', '-S', '.', '-B', self._build_dir, '-G', self._generator]
        args.extend(self._extra_gen_args)
        self._execute(args)

    def make(self):
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
        
    def run_all(self):
        self.generate()
        self.make()
        self.test()

    def _execute(self, args):
        subprocess.check_call(args)

class windows_build(build):
    def __init__(self, cmd_args):
        super(windows_build, self).__init__(cmd_args)
        self._generator = 'Visual Studio 16 2019'
        self._extra_gen_args = ['-A', 'x64']
        self._extra_build_args = ['--config', cmd_args.type]
        self._tests_target = 'RUN_TESTS'

class linux_build(build):
    def __init__(self, cmd_args):
        super(linux_build, self).__init__(cmd_args)
        self._build_dir = str(os.path.join('build', cmd_args.type.lower()))
        self._extra_gen_args = ['-DCMAKE_C_COMPILER=clang', 
                                '-DCMAKE_CXX_COMPILER=clang++',
                               f'-DCMAKE_BUILD_TYPE={cmd_args.type}']

def usage():
    parser = argparse.ArgumentParser(description='Sample wrapper for cmake.')
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument('gen', nargs='?',
                        help='run cmake configuration')
    command.add_argument('make', nargs='?',
                        help='build cmake configuration')
    command.add_argument('clean', nargs='?',
                        help='clean cmake configuration')
    command.add_argument('test', nargs='?',
                        help='run tests')
    command.add_argument('all', nargs='?',
                        help='configure, make, run tests')
    parser.add_argument('--type', action='store', default='Debug', 
                        help='build type: Debug, Release or RelWithDebInfo')
    parser.add_argument('--verbose', action='store_const', const=True, 
                        help='verbose')
    return parser.parse_args()

if __name__ == '__main__':
    operating_system = platform.system()
    if operating_system not in ['Windows', 'Linux']:
        print ('Unsupported OS')
        exit(1)

    cmd_args = usage()
    if cmd_args.type not in ['Debug', 'Release', 'RelWithDebInfo']:
        print (f'Unsupported build type: {cmd_args.type}')
        exit(2)

    build = windows_build(cmd_args) if operating_system == 'Windows' else linux_build(cmd_args)

    command = cmd_args.gen
    if (command == 'gen'):
        build.generate()
    elif (command == 'make'):
        build.make()
    elif (command == 'clean'):
        build.clean()
    elif (command == 'test'):
        build.test()
    elif (command == 'all'):
        build.run_all()
    else:
        print (f'Unsupported command: {command}')
        exit(3)
