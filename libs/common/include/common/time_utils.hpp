#ifndef CPP_PROJECT_COMMON_TIME_UTILS_H
#define CPP_PROJECT_COMMON_TIME_UTILS_H

#include <chrono>
#include <functional>

namespace cpp_project::common
{

template <typename precision = std::chrono::microseconds,
          typename clock = std::chrono::high_resolution_clock>
precision time_since(const typename clock::time_point& since)
{
    return std::chrono::duration_cast<precision>(clock::now() - since);
}

template <typename return_type = void,
          typename precision = std::chrono::microseconds,
          typename clock = std::chrono::high_resolution_clock>
std::pair<return_type, precision> measure_execution_time(const std::function<return_type()>& op)
{
    const auto start = clock::now();
    auto result = op();
    auto duration = time_since<precision, clock>(start);

    return {result, duration};
}

}  // namespace cpp_project

#endif
