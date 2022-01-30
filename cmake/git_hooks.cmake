find_package (Python3 COMPONENTS Interpreter)

if (NOT Python3_FOUND)
    message(WARNING "python3 not found, commit hooks will not be installed")
    return()
endif()

if (NOT CLANG_FORMAT_MAJOR_VERSION)
    message(WARNING "clang-format version is unknown")
    return()
elseif (CLANG_FORMAT_MAJOR_VERSION LESS CLANG_FORMAT_MIN_REQUIRED_VERSION)
    message(WARNING "clang-format is too old, will not install pre-commit hook (required: ${CLANG_FORMAT_MIN_REQUIRED_VERSION}, installed: ${CLANG_FORMAT_MAJOR_VERSION}")
    return()
endif()

set(RUN_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/scripts/Run.py)
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/scripts/pre-commit-hook
    ${CMAKE_CURRENT_SOURCE_DIR}/.git/hooks/pre-commit
    @ONLY)
