set(PROJECT_NAME invest)

project(${PROJECT_NAME})

# list the header files to show them in IDEs
# 'STATIC' is optional; if removed, it can be controlled using BUILD_SHARED_LIBS
add_library(${PROJECT_NAME} SHARED
            include/invest/stocks.h src/stocks.cpp
            src/helper.h src/helper.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC include)
target_include_directories(${PROJECT_NAME} PRIVATE include/invest)

target_link_libraries(${PROJECT_NAME} PUBLIC math)
