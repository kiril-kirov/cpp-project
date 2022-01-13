#ifndef CPP_PROJECT_LIB_INVEST_TYPES_H
#define CPP_PROJECT_LIB_INVEST_TYPES_H

namespace cpp_project::invest
{

struct candle
{
    float low_price = .0;
    float open_price = .0;
    float close_price = .0;
    float high_price = .0;
};

}  // namespace cpp_project::invest

#endif
