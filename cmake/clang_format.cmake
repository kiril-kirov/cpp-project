find_program(PYTHON3_EXECUTABLE python3)
message(STATUS ${PYTHON3_EXECUTABLE})

add_custom_target(format
    COMMAND ${PYTHON_EXECUTABLE} 
    ${CMAKE_SOURCE_DIR}/scripts/Run.py format-all
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
