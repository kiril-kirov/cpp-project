find_program(CLANG_FORMAT_EXECUTABLE clang-format)
message(STATUS "clang-format executable found: ${CLANG_FORMAT_EXECUTABLE}")

if (CLANG_FORMAT_EXECUTABLE-NOTFOUND)
    message(WARNING "clang-format is not installed, so it won't work")
else()
    file(GLOB_RECURSE ALL_SOURCE_FILES *.hpp *.cpp *.h *.hpp *.hxx *.cxx)
    list(FILTER ALL_SOURCE_FILES EXCLUDE REGEX "/external/|/build/")

    list(LENGTH ALL_SOURCE_FILES ALL_SOURCE_FILES_COUNT)
    message(STATUS "Formattable source files: ${ALL_SOURCE_FILES_COUNT}")
    add_custom_target(format
        COMMAND ${CLANG_FORMAT_EXECUTABLE}
        -style file -i ${ALL_SOURCE_FILES}
        WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()
