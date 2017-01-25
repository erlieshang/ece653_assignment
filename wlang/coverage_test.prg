x := 1;
y := 1;
if x < 0 or y = 1 then y := 2;
print_state;
havoc x, y;
x := 10;
y := 128;
skip;
if true and (x <= 20 and y >= 100)
then x := x + 1
else x := x * 2;
if x > 20 or y < 100 then x := x + 1 else x := x * 2;
if x > 25 then x := 1;
while x > 17 do {x := x - 1; y := y / 2};
assume x = 17; 
assert x = 17; 
if not false then x :=  -1 * 3 - 2 + 2; 
if true then skip;
 assert x = 23