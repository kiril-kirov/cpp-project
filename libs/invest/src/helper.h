#ifndef CPP_PROJECT_LIB_INVEST_HELPER_H
#define CPP_PROJECT_LIB_INVEST_HELPER_H

namespace cpp_project::invest
{
struct candle;

class helper
{
public:
    static float calculate_average_price(const candle& price);
};

}  // namespace cpp_project::invest

#endif
