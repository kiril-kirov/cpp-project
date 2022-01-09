include(CTest)

# Catch2 can be downloaded using FetchContent, but this brings the source inside the build directory,
# meaning - clean build will require yet another clone. So, to avoid hacky approaches or cloning on each
# clean build, the header-only lib is included in external, hence the following lines.
set(CATCH_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/external)
add_library(Catch2::Catch IMPORTED INTERFACE)
set_property(TARGET Catch2::Catch PROPERTY INTERFACE_INCLUDE_DIRECTORIES "${CATCH_INCLUDE_DIR}")
