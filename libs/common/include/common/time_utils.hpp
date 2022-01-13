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

template <typename precision = std::chrono::microseconds,
          typename clock = std::chrono::high_resolution_clock>
precision measure_execution_time(const std::function<void()>& op)
{
    const auto start = clock::now();
    op();
    return time_since<precision, clock>(start);
}

}  // namespace cpp_project

#endif
