# cpp-project

A "template" C++ project with a specific directory structure and short sample source code.

The project will be cross-platform, but some of the tools are platform-specific.

[CMake](https://cmake.org/) will be used in this project with the following generators:
* [Ninja](https://ninja-build.org/) combined with [clang](https://clang.llvm.org/) for Linux;
* [Visual Studio](https://visualstudio.microsoft.com/) for Windows.
* Xcode can be used for macOS, but it will not be included in the current project.

Compiler options:
* include (almost) all possible compiler warnings;
* treat all warnings as errors;
* two build configurations - debug and release.

A python3 build script will also be included, providing a set of commands for:
* formatting the source code;
* running all static analysis tools;
* building the project;
* running unit tests;
* running all dynamic analysis tools on the unit tests.

## External tools

All tools will be integrated with the project directory structure.
A sample configuration will also be provided for each tool.

Selected tools:
* [clang-format](https://clang.llvm.org/docs/ClangFormat.html): source code formatter;
* [clang-tidy](https://clang.llvm.org/extra/clang-tidy/): source code linter;
* [clang static analyzer](https://clang-analyzer.llvm.org/): static analysis tool;
* [cppcheck](https://github.com/danmar/cppcheck): static analysis tool;
* [clang sanitizers](https://github.com/google/sanitizers): dynamic analysis tools; Address-, Leak-, Memory- and ThreadSanitizer will be used;
* [valgrind](https://valgrind.org/): dynamic analysis (Linux-specific) tool; Memcheck and Callgrind will be used;
* [gcc](https://gcc.gnu.org/): take advantage of most gcc warnings, including `-Weffc++`; used with  `-fsyntax-only`; Linux-specific.

The idea of combining so many tools (some of them - platform specific) is to catch as many bugs as possible in advance.

## 3-rd party libraries

The main goal is to choose and demonstrate a set of a few 3-rd party libraries, which are usually used in a C++ project.
The criterias are:
* have all the usual/basic features one would expect from such libraries;
* new versions are recently released (i.e. it's currently maintained, not long-forgotten);
* popular and widely used;
* cross-platform;
* fast and lightweight.

In general, I'd avoid using heavy artillery libraries like boost (unless needed, of course).
If you already have a boost dependency, ignore this section and use the boost equivalents instead (hinted in parentheses).

* unit tests: [Catch2](https://github.com/catchorg/Catch2) (or [Boost.Test](https://www.boost.org/doc/libs/1_75_0/libs/test/doc/html/index.html));
* logger: [spdlog](https://github.com/gabime/spdlog) (or [Boost.Log](https://www.boost.org/doc/libs/1_75_0/libs/log/doc/html/index.html));
* command line arguments: [cxxopts](https://github.com/jarro2783/cxxopts) (or [Boost.Program_options](https://www.boost.org/doc/libs/1_75_0/doc/html/program_options.html)).
