set(PROJECT_NAME common)

project(${PROJECT_NAME})

# example for header-only lib
add_library(${PROJECT_NAME} INTERFACE)

# hack to show the header-only project in VS
add_custom_target(${PROJECT_NAME}_ SOURCES include/common/time_utils.hpp
                                           include/common/fp_utils.hpp)

target_include_directories(${PROJECT_NAME} INTERFACE include)
