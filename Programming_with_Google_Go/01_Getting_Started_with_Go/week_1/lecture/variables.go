package main

import "fmt"

func main() {
	//Variables
	var x int
	var a, b int // can declare many on the same line
	var s string

	fmt.Println("x", x)
	fmt.Println("a", a, "b", b)
	fmt.Println("s", s)

	//Type Declaration
	type Celsius float64
	type IDnum int

	var temp Celsius
	var pid IDnum

	fmt.Println("temp", temp)
	fmt.Println("pid", pid)

	//Initializing Variables
	var y int = 100 // initialize in the declaration
	var z = 100
	var h = "Hello"
	var e, r = 10, 20

	fmt.Println("y", y)
	fmt.Println("z", z)
	fmt.Println("h", h)
	fmt.Println("e", e, "r", r)

	var k int // initialize after the declaration
	k = 100

	fmt.Println("k", k)

	//Short Variable Declaration
	v := 100

	fmt.Println("v", v)
}
