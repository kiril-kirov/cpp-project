#ifndef CPP_PROJECT_LIB_INVEST_STOCKS_H
#define CPP_PROJECT_LIB_INVEST_STOCKS_H

#include "types.h"

#include <vector>

namespace cpp_project::invest
{

class stocks
{
public:
    // ordered
    stocks& feed_history(const candle& price);
    stocks& feed_history(candle&& price);

    float calculate_average_price() const;

private:
    using price_history = std::vector<candle>;
    price_history history;
};

}  // namespace cpp_project::invest

#endif
