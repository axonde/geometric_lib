# GEOMETRIC LIB!
This lib give you ready-to-use functions for geometric calculations and powerful calculator (console program).
The calculator have a simple CLI, which you can easily help doing your geometric tasks.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Functions
## `area(number)`
Avaible shapes: circle, square and triangle.
Return a number, who is a area of a geometric figure.
Example:
```python
area(5) # 25
```

## `perimeter(number)`
Avaible shapes: circle, square and triangle.
Return a number, who is a perimiter of a geometric figure.
```python
perimiter(5)  # 20
```

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

## Short project history
86edb1c L-05: Update Docs. Add user agreement info
438b89a L-05: Add user agreement
6adb962 L-03: Docs added
3049431 L-04: Add rectangle.py
b5b0fae L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
