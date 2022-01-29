import os
import sys
import subprocess
import enum

class Scope (enum.Enum):
    LOCAL  = 1,
    BRANCH = 2,
    ALL    = 3

class Formatter:
    def __init__(self, scope, build_dir):
        self._scope = scope
        self._build_dir = build_dir

    def run(self):
        if self._scope == Scope.LOCAL:
            self._format_local()
        elif self._scope == Scope.BRANCH:
            self._format_branch()
        else:
            assert self._scope == Scope.ALL
            self._format_all()

    def _format_local(self):
        local_changes = self._execute(['git', 'status', '--porcelain'])

        locally_modified_files = []
        for change in local_changes:
            status, file = change[:3], change[3:]
            if status.find('D') == -1 and self._is_cxx_file(file):
                locally_modified_files.append(file)

        self._format_files(locally_modified_files)

    def _format_branch(self):
        branch_changes = self._execute(['git', 'diff', '--name-only', '--diff-filter', 'd', 'main'])

        modified_files = [f for f in branch_changes if self._is_cxx_file(f)]

        self._format_files(modified_files)

    def _format_all(self):
        cmake_args = ['cmake', '--build', self._build_dir, '--target', 'format']
        self._execute(cmake_args)

    def _format_files(self, files):
        if not files:
            print(f'Files for formatting not found')
            return
        print(f'Formatting {len(files)} C++ files...')
        
        clang_command = ['clang-format', '-style', 'file', '-i']
        for f in files:
            self._execute(clang_command + [str(f)])
        
        print(f'Done')

    def _execute(self, args):
        return subprocess.check_output(args).decode().split('\n')

    def _is_cxx_file(self, filename):
        return filename.split('.')[-1] in ['h', 'c', 'hpp', 'cpp', 'hxx', 'cxx']
