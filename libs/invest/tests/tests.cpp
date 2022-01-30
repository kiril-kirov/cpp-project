#include "invest/stocks.h"

#include "common/fp_utils.hpp"

#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"

using namespace cpp_project::invest;
using namespace cpp_project::common;

TEST_CASE("average", "invest")
{
    stocks company;
    company.feed_history({1.1f, 1.2f, 1.3f, 1.4f})
        .feed_history({1.2f, 1.3f, 1.4f, 1.6f})
        .feed_history({1.20f, 1.3f, 1.3f, 1.3f});

    REQUIRE(equal(company.calculate_average_price(), 1.3f));
}
