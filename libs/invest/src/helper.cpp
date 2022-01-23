#include "helper.h"

#include "types.h"

namespace cpp_project::invest
{

float helper::calculate_average_price(const candle& price)
{
    return (price.low_price + price.open_price + price.close_price + price.high_price) / 4;
}

}  // namespace cpp_project::invest
