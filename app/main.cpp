#include "invest/stocks.h"
#include "common/time_utils.hpp"
#include <iostream>

using namespace cpp_project::invest;
using namespace cpp_project::common;
using ns = std::chrono::nanoseconds;

int main()
{
    stocks company;
    company.
        feed_history({ 1.1f, 1.2f, 1.3f, 1.4f}).
        feed_history({ 1.2f, 1.3f, 1.4f, 1.6f}).
        feed_history({ 1.1f, 1.2f, 1.3f, 1.4f}).
        feed_history({ 1.2f, 1.4f, 1.4f, 1.5f}).
        feed_history({ 1.1f, 1.3f, 1.3f, 1.4f});

    float avg_price = .0;
    const auto duration = measure_execution_time<ns>([&company, &avg_price] () { 
        avg_price = company.calculate_average_price(); 
    });
    std::cout << "Average price: " << avg_price << " (execution time: " << duration.count() << "ns)" << std::endl;
}
