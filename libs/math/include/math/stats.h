#ifndef CPP_PROJECT_LIB_MATH_STATS_H
#define CPP_PROJECT_LIB_MATH_STATS_H

#include <vector>

namespace cpp_project::stats
{

float average(const std::vector<float>& points);

float median(std::vector<float> points);
float median_sorted(const std::vector<float>& points);

}  // namespace cpp_project::stats

#endif
