set(PROJECT_NAME common)

project(${PROJECT_NAME})

# example for header-only lib
add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(${PROJECT_NAME} INTERFACE include)
