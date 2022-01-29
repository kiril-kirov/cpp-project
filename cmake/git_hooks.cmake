find_program(PYTHON3_EXECUTABLE python3)
if (PYTHON3_EXECUTABLE-NOTFOUND)
    message(WARNING "python3 not found, commit hooks will not be installed")
else()
    set(RUN_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/scripts/Run.py)
    configure_file(
        ${CMAKE_CURRENT_SOURCE_DIR}/scripts/pre-commit-hook
        ${CMAKE_CURRENT_SOURCE_DIR}/.git/hooks/pre-commit
        @ONLY)
endif()
