import Build
import Format

import os
import sys
import platform
import argparse

def define_arguments():
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
    command.add_argument('format', nargs='?', 
                        help='format source code; use in combination with --changes')
    command.add_argument('analyze-static', nargs='?', 
                        help='run static code analysis; use in combination with --changes')
    command.add_argument('all', nargs='?',
                        help='equivalent to configure, make, run tests')

    parser.add_argument('--type', action='store', default='Debug',
                        choices=['Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'],
                        help='build type')
    parser.add_argument('--changes', action='store', default='local',
                        choices=['local', 'branch', 'all'],
                        help='''choose local changes, branch changes or all source files; 
                                combine with "format" or "analyze-static"''')
    parser.add_argument('--verbose', action='store_const', const=True,
                        help='verbose')

    return parser

if __name__ == '__main__':
    operating_system = platform.system()
    if operating_system not in ['Windows', 'Linux']:
        sys.exit(f'Unsupported OS: {operating_system}')

    args_definition = define_arguments()
    cmd_args = args_definition.parse_args()

    builder = Build.WindowsBuild(cmd_args) if operating_system == 'Windows' else Build.LinuxBuild(cmd_args)

    try:
        command = cmd_args.gen
        if (command == 'gen'):
            builder.generate()
        elif (command == 'make'):
            if not os.path.exists(builder.build_dir()):
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
            scope = Format.Scope[cmd_args.changes.upper()]
            Format.Formatter(scope=scope, build_dir=builder.build_dir()).run()
        elif (command == 'analyze-static'):
            scope = Format.Scope[cmd_args.changes.upper()]
            Format.Formatter(scope=scope, build_dir=builder.build_dir(), check_only=True).run()
        else:
            args_definition.print_help()
            args_definition.exit(f'\nUnsupported command: {command}')
    except Exception as e:
        print(f'\n{e}')
        sys.exit(1)
