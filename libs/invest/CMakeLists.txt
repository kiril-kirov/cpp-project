set(PROJECT_NAME invest)

project(${PROJECT_NAME})

add_library(${PROJECT_NAME} STATIC
            include/invest/stocks.h src/stocks.cpp
            src/helper.h src/helper.cpp)

target_include_directories(${PROJECT_NAME}
                            PUBLIC
                                include
                            PRIVATE
                                include/invest)

target_link_libraries(${PROJECT_NAME} PUBLIC math)

add_unit_tests(${PROJECT_NAME})
