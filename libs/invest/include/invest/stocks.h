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
    stocks& feed_history(const price_point& price);
    stocks& feed_history(price_point&& price);

    float average_price() const;

private:
    using stocks_container = std::vector<price_point>;
    stocks_container history;
};

}  // namespace cpp_project::invest

#endif
