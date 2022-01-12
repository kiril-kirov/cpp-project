set(PROJECT_NAME math)

project(${PROJECT_NAME})

add_library(${PROJECT_NAME} STATIC
            include/math/stats.h src/stats.cpp)

target_include_directories(${PROJECT_NAME}
                            PUBLIC
                                include
                            PRIVATE
                                include/math)

add_unit_tests(${PROJECT_NAME})
