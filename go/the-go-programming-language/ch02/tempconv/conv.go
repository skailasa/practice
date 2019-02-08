package tempconv

// CtoF converts from Celcius to Fahrenheit
func CtoF(c Celcius) Fahrenheit {return Fahrenheit(c*9/5 + 32)}

// FtoC does the reverse
func FtoC(f Fahrenheit) Celcius {return Celcius((f-32)*5/9)}

func CtoK(c Celcius) Kelvin {return Kelvin(c+FreezingK)}