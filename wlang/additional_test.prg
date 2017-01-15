x := 10;
y := 128;
print_state;
skip;
if x < 20 and y > 100 then x := x + 1 else x := x * 2;
if x > 20 or y < 100 then x := x + 1 else x := x * 2;
while x > 17 do {x := x - 1; y := y / 2};
print_state