// Performs celcius/fahrenheit conversions

package tempconv

import "fmt"

type Celcius float64
type Fahrenheit float64
type Kelvin float64

const (
	AbsoluteZeroX Celcius = -273.5
	FreezingC Celcius = 0
	BoilingC Celcius = 100
	FreezingK Celcius = 273.5
)

func (c Celcius) String() string {return fmt.Sprintf("%gC", c)}
func (f Fahrenheit) String() string {return fmt.Sprintf("%gF", f)}
func (k Kelvin) String() string {return fmt.Sprintf("%gK", k)}