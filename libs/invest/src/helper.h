#ifndef CPP_PROJECT_LIB_INVEST_HELPER_H
#define CPP_PROJECT_LIB_INVEST_HELPER_H

// fwd declarations
namespace cpp_project::invest
{
struct candle;
}

namespace cpp_project::invest
{

class helper
{
public:
    static float average_price(const candle& price);
};

}

#endif
