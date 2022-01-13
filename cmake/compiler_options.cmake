# warnings
if (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    add_compile_options(/W4 /WX)  # /Wall is unusable due to warnings in the standard libs
else()
    if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
        add_compile_options(-Wall -Wextra -pedantic)
    else(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        add_compile_options(-Weverything)
        add_compile_options(-Wno-c++98-c++11-c++14-compat)
        add_compile_options(-Wno-c++98-compat)
    endif()
    add_compile_options(-Werror)
endif()

# optimization flags
if (NOT CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    add_compile_options("$<$<CONFIG:Release>:-O3>")         # usually a default
    add_compile_options("$<$<CONFIG:RelWithDebInfo>:-O3>")  # make RelWithDebInfo optimizations same as Release
endif()
