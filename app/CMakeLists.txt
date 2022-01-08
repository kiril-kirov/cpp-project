set(PROJECT_NAME app)

project(${PROJECT_NAME})

# list the header files to show them in IDEs
add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(${PROJECT_NAME} PRIVATE invest common)

