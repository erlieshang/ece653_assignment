x := 10;
y := 128;
skip;
if x < 20 and y > 100 then x := x + 1 else x := x * 2;
if x > 20 or y < 100 then x := x + 1 else x := x * 2;
if x > 25 then x := 1;
while x > 17 do {x := x - 1; y := y / 2};
print_state;
assert x = 17;
if not x > 25 then x := 1;
havoc x;
assert x = 23;
print_state