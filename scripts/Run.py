from Build import WindowsBuild, LinuxBuild
from Format import Formatter, Scope

from os import path
from sys import exit
from platform import system
from argparse import ArgumentParser

def define_arguments():
    parser = ArgumentParser(description='Wraps and extends the cmake usage capabilities')

    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument('gen', nargs='?', help='run cmake configuration')
    command.add_argument('make', nargs='?', help='build cmake configuration')
    command.add_argument('clean', nargs='?', help='clean cmake configuration')
    command.add_argument('test', nargs='?', help='run tests')
    command.add_argument('format', nargs='?', help='format source code')
    command.add_argument('analyze-static', nargs='?', help='run static code analysis')
    command.add_argument('all', nargs='?', help='equivalent to configure, make, run tests')

    build_type = parser.add_mutually_exclusive_group(required=False)
    build_type.add_argument('-d', '--debug', action='store_true', help='use debug configuraion [default]')
    build_type.add_argument('-r', '--release', action='store_true', help='use release configuraion')
    build_type.add_argument('-i', '--relwithdebinfo', action='store_true', help='use RelWithDebInfo configuraion')
    build_type.add_argument('-s', '--minsizerel', action='store_true', help='use MinSizeRel configuraion')

    changes = parser.add_mutually_exclusive_group(required=False)
    changes.add_argument('-l', '--local', action='store_true',
                        help='[format|analyze-static] only locally modified files [default]')
    changes.add_argument('-b', '--branch', action='store_true',
                        help='[format|analyze-static] files, modified in the current branch')
    changes.add_argument('-a', '--all', action='store_true',
                        help='[format|analyze-static] all source files')

    parser.add_argument('-v', '--verbose', action='store_const', const=True,
                        help='verbose')

    return parser

def parse_build_type(cmd_args):
    if cmd_args.release:
        return 'Release'
    if cmd_args.relwithdebinfo:
        return 'RelWithDebInfo'
    if cmd_args.minsizerel:
        return 'MinSizeRel'
    return 'Debug'  # default

def create_builder(cmd_args):
    verbose = cmd_args.verbose
    build_type = parse_build_type(cmd_args)
    return WindowsBuild(build_type, verbose) if operating_system == 'Windows' else LinuxBuild(build_type, verbose)

def parse_changes(cmd_args):
    if cmd_args.all:
        return Scope.ALL
    if cmd_args.branch:
        return Scope.BRANCH
    return Scope.LOCAL  # default

if __name__ == '__main__':
    operating_system = system()
    if operating_system not in ['Windows', 'Linux']:
        exit(f'Unsupported OS: {operating_system}')

    args_definition = define_arguments()
    cmd_args = args_definition.parse_args()

    builder = create_builder(cmd_args)

    command = cmd_args.gen
    try:
        if (command == 'gen'):
            builder.generate()
        elif (command == 'make'):
            if not path.exists(builder.build_dir()):
                builder.generate()
            builder.make()
        elif (command == 'clean'):
            builder.clean()
        elif (command == 'test'):
            builder.test()
        elif (command == 'all'):
            builder.generate()
            builder.make()
            builder.test()
        elif (command == 'format'):
            scope = parse_changes(cmd_args)
            Formatter(scope=scope, build_dir=builder.build_dir()).run()
        elif (command == 'analyze-static'):
            scope = parse_changes(cmd_args)
            Formatter(scope=scope, build_dir=builder.build_dir(), check_only=True).run()
        else:
            args_definition.print_help()
            args_definition.exit(f'\nUnsupported command: {command}')
    except Exception as e:
        print(f'\n{e}')
        exit(1)
