#include "invest/stocks.h"
#include "common/time_utils.hpp"
#include <iostream>

using namespace cpp_project::invest;
using namespace cpp_project::common;

int main()
{
    stocks company;
    company.
        feed_history(price_point{{ 3, 1, 2022 }, { 1.1f, 1.2f, 1.3f, 1.4f}}).
        feed_history(price_point{{ 4, 1, 2022 }, { 1.2f, 1.3f, 1.4f, 1.6f}}).
        feed_history(price_point{{ 5, 1, 2022 }, { 1.1f, 1.2f, 1.3f, 1.4f}}).
        feed_history(price_point{{ 6, 1, 2022 }, { 1.2f, 1.4f, 1.4f, 1.5f}}).
        feed_history(price_point{{ 7, 1, 2022 }, { 1.1f, 1.3f, 1.3f, 1.4f}});

    using us = std::chrono::microseconds;
    const auto [avg_price, duration] = measure_execution_time<float, us>([&company]{ return company.average_price(); });
    std::cout << "Average price: " << avg_price << " (execution time: " << duration.count() << "ns)" << std::endl;
}
