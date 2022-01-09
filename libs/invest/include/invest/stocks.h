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

    float average_price() const;

private:
    using stocks_container = std::vector<candle>;
    stocks_container history;
};

}  // namespace cpp_project::invest

#endif
