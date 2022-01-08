set(PROJECT_NAME math)

project(${PROJECT_NAME})

# list the header files to show them in IDEs
# 'STATIC' is optional; if removed, it can be controlled using BUILD_SHARED_LIBS
add_library(${PROJECT_NAME} STATIC
            include/math/stats.h src/stats.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC include)
target_include_directories(${PROJECT_NAME} PRIVATE include/math)

