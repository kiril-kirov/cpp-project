set(CLANG_FORMAT_MIN_REQUIRED_VERSION 12)

find_program(CLANG_FORMAT_EXECUTABLE clang-format)

if (CLANG_FORMAT_EXECUTABLE-NOTFOUND)
    message(WARNING "clang-format is not installed, will not create 'format' target")
    return()
endif()
message(STATUS "clang-format executable found: ${CLANG_FORMAT_EXECUTABLE}")

execute_process(COMMAND ${CLANG_FORMAT_EXECUTABLE} --version
                OUTPUT_VARIABLE CLANG_FORMAT_VERSION_OUTPUT
                ERROR_QUIET
                OUTPUT_STRIP_TRAILING_WHITESPACE)
if (NOT CLANG_FORMAT_VERSION_OUTPUT MATCHES "^clang-format version .*")
    message(WARNING "Cannot parse clang-format version, will not create 'format' target")
    return()
endif()

string(REGEX REPLACE "clang-format version ([0-9]+).*" "\\1"
        CLANG_FORMAT_MAJOR_VERSION "${CLANG_FORMAT_VERSION_OUTPUT}")
if(CLANG_FORMAT_MAJOR_VERSION LESS CLANG_FORMAT_MIN_REQUIRED_VERSION)
    message(WARNING "clang-format is too old, will not create 'format' target (required: ${CLANG_FORMAT_MIN_REQUIRED_VERSION}, installed: ${CLANG_FORMAT_MAJOR_VERSION}")
    return()
endif()

file(GLOB_RECURSE ALL_SOURCE_FILES *.hpp *.cpp *.h *.hpp *.hxx *.cxx)
list(FILTER ALL_SOURCE_FILES EXCLUDE REGEX "/external/|/build/")

list(LENGTH ALL_SOURCE_FILES ALL_SOURCE_FILES_COUNT)
message(STATUS "Formattable source files: ${ALL_SOURCE_FILES_COUNT}")
add_custom_target(format
    COMMAND ${CLANG_FORMAT_EXECUTABLE}
    -style file -i ${ALL_SOURCE_FILES}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    VERBATIM)
