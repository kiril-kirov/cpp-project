#include "math/stats.h"
#include "common/fp_utils.hpp"

#define CATCH_CONFIG_MAIN
#include "catch2/catch.hpp"

#include <numeric>
#include <cmath>

using namespace cpp_project::stats;
using namespace cpp_project::common;

TEST_CASE("average", "stats")
{
    REQUIRE(equal(average({ 1.1f }), 1.1f));
    REQUIRE(equal(average({ 1.1f, 3.3f }), 2.2f));
    REQUIRE(equal(average({1.f, 2.f, 3.f, 4.f}), 2.5f));
}

TEST_CASE("median", "stats")
{
    REQUIRE(equal(median({ 1.1f }), 1.1f));
    REQUIRE(equal(median({ 1.1f, 3.3f }), 2.2f));

    REQUIRE(equal(median({1.1f, 1.2f, 20.f, 30.f, 50.f}), 20.f));
    REQUIRE(equal(median({1.1f, 1.2f, 20.f, 30.f, 50.f, 55.f}), 25.f));
}
