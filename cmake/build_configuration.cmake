if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "Choose the type of build." FORCE)
endif()

string(TOUPPER ${CMAKE_BUILD_TYPE} upper_build_type)
set(cflags_var "CMAKE_C_FLAGS_${upper_build_type}")
set(cxxflags_var "CMAKE_CXX_FLAGS_${upper_build_type}")

message(STATUS "C++ compiler flags: ${${cxxflags_var}}")
message(STATUS "C compiler flags: ${${cflags_var}}")
