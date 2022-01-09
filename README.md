# cpp-project

A "template"/canonical C++ project with a specific directory structure and short sample source code.

## General idea

The project will be cross-platform, but some of the tools will be platform-specific.

[CMake](https://cmake.org/) will be used in this project with the following generators:
* [Ninja](https://ninja-build.org/) combined with [clang](https://clang.llvm.org/) for Linux;
* [Visual Studio](https://visualstudio.microsoft.com/) for Windows;
* Xcode can be used for macOS, but it will not be included in the current project.

Compiler options:
* include (almost) all possible compiler warnings;
* treat all warnings as errors;
* two build configurations - debug and release.

Several tools will be introduced (see below). All of them will be integrated with cmake.  
A python3 wrapper script will be included.

### External tools

All tools will be integrated with the project directory structure.
A sample configuration will also be provided for each tool.

Selected tools:
* [clang-format](https://clang.llvm.org/docs/ClangFormat.html): source code formatter;
* [clang-tidy](https://clang.llvm.org/extra/clang-tidy/): source code linter;
* [clang static analyzer](https://clang-analyzer.llvm.org/): static analysis tool;
* [cppcheck](https://github.com/danmar/cppcheck): static analysis tool;
* [clang sanitizers](https://github.com/google/sanitizers): dynamic analysis tools; Address-, Leak-, Memory- and ThreadSanitizer will be used;
* [valgrind](https://valgrind.org/): dynamic analysis (Linux-specific) tool; Memcheck and Callgrind will be used;
* [gcc](https://gcc.gnu.org/): take advantage of most gcc warnings, including `-Weffc++`; used with  `-fsyntax-only`; Linux-specific;
* [doxygen](https://www.doxygen.nl/index.html): tool for automatic documentation generation;
* TODO code coverage (??) .

The idea of combining so many tools (some of them - platform specific) is to catch as many bugs as possible in advance.

### 3-rd party libraries

The main goal is to choose and demonstrate a set of a few 3-rd party libraries, which are usually used in a C++ project.
The criterias are:
* have all the usual/basic features one would expect from such libraries;
* new versions are recently released (i.e. it's currently maintained, not long-forgotten);
* popular and widely used;
* cross-platform;
* fast and lightweight.

In general, I'd avoid using heavy artillery libraries like boost (unless needed, of course).
If you already have a boost dependency, ignore this section and use the boost equivalents instead (hinted in parentheses).

* unit tests: [Catch2](https://github.com/catchorg/Catch2) (or [Boost.Test](https://www.boost.org/doc/libs/1_75_0/libs/test/doc/html/index.html)); combine with [CMake's ctest](https://cmake.org/cmake/help/latest/manual/ctest.1.html) to allow parallel execution of unit tests and easy integration with the build system;
* logger: [spdlog](https://github.com/gabime/spdlog) (or [Boost.Log](https://www.boost.org/doc/libs/1_75_0/libs/log/doc/html/index.html));
* command line arguments: [cxxopts](https://github.com/jarro2783/cxxopts) (or [Boost.Program_options](https://www.boost.org/doc/libs/1_75_0/doc/html/program_options.html)).

### My environment

I use Windows, combined with [WSL](https://docs.microsoft.com/en-us/windows/wsl/install).
This gives me the ability to easily switch between the two operating systems and build/test/analyze the project on both of them (using the platform-specific tools).

## HOWTOs

Everything is tightly integrated with the `cmake` build system.  
If you know how to work with `cmake` - feel free to use it directly, it's the most flexible way.

For sample `cmake` commands, check `scripts/make.py` - it's a very simple helper script, that wraps the `cmake` usage. It supports Windows and Linux only. It's not flexible, but it covers some basic usages and it's easier for using than directly writing `cmake` commands.

## Progress

This is a work-in-progress project. All of the above is just the current plan. The TODO list is below.

Next introduce:
* clang-format (formatter);
* clang-tidy (static analysis);
* clang static analyzer;
* cppcheck (static analysis);
* valgrind (dynamic analysis);
* clang sanitizers (dynamic analysis);
* \[optional\] gcc with -Weffc++ and max warnings; use with -fsyntax-only;
* update the HOWTOs section.

This will be version 0.2 (git tag) - extends 0.1 with static/dynamic code analysis tools.

Next:
* doxygen: automatic documentation generation;
* consider adding a tool (requires a research) for code coverage analysis;
* consider adding include-what-you-use;
* consider using precompiled header for the unit test library.

This will be version 0.3 (git tag) - extends 0.2 with nice-to-have tools.

Finally introduce:
* logger: spdlog; add it in the unit tests for demo purposes;
* command line arguments parser: cxxopts; add help and other sample options.

Something interesting came out, so review [Use the tools available](https://lefticus.gitbooks.io/cpp-best-practices/content/02-Use_the_Tools_Available.html)

This will be version 1.0 - the first complete version for a C++ project template.
