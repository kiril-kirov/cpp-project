#ifndef CPP_PROJECT_LIB_INVEST_TYPES_H
#define CPP_PROJECT_LIB_INVEST_TYPES_H

#include <cstdint>

namespace cpp_project::invest
{
struct date
{
    std::uint8_t day = {};
    std::uint8_t month = {};
    std::uint16_t year = {};
};

struct candle
{
    float low_price = .0;
    float open_price = .0;
    float close_price = .0;
    float high_price = .0;
};

struct price_point
{
    date when;
    candle price;
};

}  // namespace cpp_project::invest

#endif
