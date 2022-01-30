#ifndef CPP_PROJECT_COMMON_FP_UTILS_H
#define CPP_PROJECT_COMMON_FP_UTILS_H

#include <cmath>
#include <limits>
#include <type_traits>

namespace cpp_project::common
{

template<typename T, typename std::enable_if<std::is_floating_point<T>::value>::type* = nullptr>
bool equal(T lhs, T rhs)
{
    return std::fabs(lhs - rhs) <= std::numeric_limits<T>::epsilon();
}

}  // namespace cpp_project::common

#endif
