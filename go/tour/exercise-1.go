/*
Implement a square root function by making repeated approximations
in a for loop using the Newton method.
 */
package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) float64 {
	/*
	Find the square root of a number iteratively
	Stop iteration once root accuracy reaches defined
	threshold
	 */
	z := 1.
	n_iter := 100
	_cached_value := 0.
	thresh := 0.0000001

	for i := 0 ; i < n_iter; i ++ {
		diff := math.Abs(z - (z*z-x)/(2*z) - _cached_value)

		if diff < thresh {
			fmt.Println(i)
			break
		}
		z -= (z*z-x)/(2*z)
		_cached_value = z
		}
	return z
}

func main() {
	fmt.Println(sqrt(2.0))
}

