cmake_minimum_required(VERSION 3.16)

set(PROJECT_NAME cpp_project)

cmake_policy(SET CMP0054 NEW)

project(${PROJECT_NAME} VERSION 0.1
                        DESCRIPTION "A sample C++ project with integrated common tools"
                        LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set_property(GLOBAL PROPERTY USE_FOLDERS ON)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/" ${CMAKE_MODULE_PATH})
include(build_configuration)
include(compiler_options)
include(git_hooks)
include(clang_format)
include(unit_tests)

add_subdirectory(libs)
add_subdirectory(app)
