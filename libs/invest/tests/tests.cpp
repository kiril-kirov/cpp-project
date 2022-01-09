#include "invest/stocks.h"
#include "common/fp_utils.hpp"

#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"

using namespace cpp_project::invest;
using namespace cpp_project::common;

TEST_CASE("average", "invest")
{    
    stocks company;
    company.
        feed_history({ 1.1f, 1.2f, 1.3f, 1.4f}).   // 1.25
        feed_history({ 1.2f, 1.3f, 1.4f, 1.6f}).   // 1.375
        feed_history({ 1.20f, 1.3f, 1.3f, 1.3f});  // 1.275

    REQUIRE(equal(company.average_price(), 1.3f));
}
