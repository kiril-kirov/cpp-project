set(PROJECT_NAME math_tests)

project(${PROJECT_NAME})

add_executable(${PROJECT_NAME} tests.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE math common Catch2::Catch)

# integrate with ctest
add_test(NAME ${PROJECT_NAME} COMMAND ${PROJECT_NAME})
