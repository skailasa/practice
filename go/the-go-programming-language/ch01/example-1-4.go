// Lissajous figure gif
package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
)

// Initialise slice
var palette = []color.Color{color.Black, color.RGBA{12, 233, 137, 1}}

const (
	blackIndex = 0 // first colour in palette
	greenIndex = 1 // second colour in palette
)

func main() {
	lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
	const (
		cycles = 5 // Number of complete x oscillator revolutions
		res = 0.001 // angular resolution
		size = 100 // image canvas covers [-size ... size]
		nframes = 64 // number of animation frames
		delay = 8 // delay beteween frames in 10ms units
	)

	freq := rand.Float64() * 3.0 // relative frequency of y-oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), greenIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim)
}