#include "stocks.h"
#include "helper.h"
#include "math/stats.h"
#include <algorithm>
#include <iterator>

using namespace std;

namespace cpp_project::invest
{

stocks& stocks::feed_history(const candle& price)
{
     history.emplace_back(price);
     return *this;
}

stocks& stocks::feed_history(candle&& price)
{
     history.emplace_back(move(price));
     return *this;
}

float stocks::average_price() const
{
    std::vector<float> avg_price_points;
    avg_price_points.reserve(history.size());
    std::transform(history.begin(), history.end(), std::back_inserter(avg_price_points),
                   [](const auto& p) { return helper::average_price(p); });

    return stats::average(avg_price_points);
}

}

