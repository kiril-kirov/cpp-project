#include "stats.h"
#include <cassert>
#include <numeric>
#include <algorithm>

using namespace std;

namespace cpp_project::stats
{

float average(const vector<float>& points)
{
    assert(!points.empty());

    const auto sum = accumulate(points.begin(), points.end(), 0.);
    return sum / points.size();
}

float median(vector<float> points)
{
    assert(!points.empty());

    sort(points.begin(), points.end());
    return median_sorted(points);
}

float median_sorted(const vector<float>& points)
{
    assert(!points.empty());

    const auto num_points = points.size();
    if (num_points == 1)
        return points.front();

    if (num_points == 2)
    {
        const auto sum = points.front() + points.back();
        return sum / 2;
    }

    const auto mid = points.size() / 2;
    if (points.size() % 2 == 1)
        return points[mid];

    return (points[mid - 1] + points[mid] + 1) / 2;
}
}
