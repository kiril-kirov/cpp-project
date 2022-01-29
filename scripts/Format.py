import enum
import subprocess

class Scope (enum.Enum):
    LOCAL  = 1,
    BRANCH = 2,
    ALL    = 3

class Formatter:
    def __init__(self, scope, build_dir, check_only=False):
        self._scope = scope
        self._build_dir = build_dir
        self._check_only = check_only

    def run(self):
        if self._scope == Scope.LOCAL:
            self._format_local()
        elif self._scope == Scope.BRANCH:
            self._format_branch()
        else:
            assert self._scope == Scope.ALL
            self._format_all()

    def _format_local(self):
        local_changes = self._execute(['git', 'status', '--porcelain']).split('\n')

        locally_modified_files = []
        for change in local_changes:
            status, file = change[:3], change[3:]
            if status.find('D') == -1 and self._is_cxx_file(file):
                locally_modified_files.append(file)

        self._format_files(locally_modified_files)

    def _format_branch(self):
        branch_changes = self._execute(['git', 'diff', '--name-only', '--diff-filter', 'd', 'main'])

        modified_files = [f for f in branch_changes.split('\n') if self._is_cxx_file(f)]

        self._format_files(modified_files)

    def _format_all(self):
        print(f'Executing cmake target "format"...')

        cmake_args = ['cmake', '--build', self._build_dir, '--target', 'format']
        self._execute(cmake_args)

        print(f'Done')

    def _format_files(self, files):
        action = 'Analyzing' if self._check_only else 'Formatting'
        if not files:
            print(f'Files for {action.lower()} not found')
            return
        print(f'{action} {len(files)} C++ file(s)...')
        
        clang_command = ['clang-format', '-style', 'file']
        if self._check_only:
            clang_command.extend(['--dry-run', '--Werror'])
        else:
            clang_command.append('-i')

        for f in files:
            self._execute(clang_command + [str(f)])
        
        print(f'Done')

    def _execute(self, args):
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = p.communicate()
        if p.returncode != 0:
            print(f'{output.decode()}' + '\n' if not error else f'---\n{error.decode()}\n')
            raise RuntimeError(f'Failed to execute the command {args}')
        else:
            return output.decode()

    def _is_cxx_file(self, filename):
        return filename.split('.')[-1] in ['h', 'c', 'hpp', 'cpp', 'hxx', 'cxx']
