/*
Testing with Mocha
 */

const assert = require('assert');

function pow(x, n) {

    if (n < 0) {
        return NaN;
    } else if (Math.round(n) != n) {
        return NaN;
    } else if (n === 0) {
        return 1;
    }

    let res = 1;

    for (let i = 0; i < n; i++) {
        res *= x;
    }
    return res;
}

describe('pow', function () {

    describe("raises x to power 3", function () {
        function makeTest(x) {
            let expected = x * x * x;
            it(`${x} to the power 3 is ${expected}`, function() {
                assert.strictEqual(pow(x, 3), expected);
            });
        }

        for (let x = 1; x <= 5; x++) {
            makeTest(x);
        }
    });

    describe("invalid powers and bases", function () {
        it("negative n should result in NaN", function () {
            assert(isNaN(pow(2, -1)));
        });
        it('fractional n should result in NaN', function () {
           assert(isNaN(pow(2, 1.5)));
        });
    })

});
