t = """111111111111111111
1x0010000000000001
111011101111111101
101010000100000001
101011010101111111
101000010100001001
100011110101111101
101110010100000001
100000000101101111
101101111100100001
101001000000101001
101101111111101001
101000000000001001
101011110100101001
101000010111111001
111011110100000001
101000000101111111
101011110101010101
1000000101000000#1
111111111111111111"""

wall = u"\u2588"
path = " "
start_char = u"\u25b2"
end_char = u"\u2605"
t = t.replace("1", wall)
t = t.replace("0", path)
t = t.replace("x", start_char)
t = t.replace("#", end_char)

t = t.split("\n")

w =  len(t[0])
h =  len(t)

testing = True

if testing:
    print("width =",w)
    print("height =", h)

m =[]

for y in range(h):
    m.append([])
    for x in range(w):
        m[y].append([])
        m[y][x] = t[y][x]

def view():
    wd = 5
    for y in range(h):
        for x in range(w):
            if m[y][x] == start_char:
                print("{:^{wd}}".format(m[y][x],wd=wd), end="")
            elif m[y][x] == end_char:
                print("{:^{wd}}".format(m[y][x],wd=wd), end="")
            elif m[y][x] == wall:
                print(m[y][x]*wd,end ="")
            else:
                print("{:{wd}}".format(m[y][x],wd=wd), end="")
        print()

view()
print()

val = 0

def go(cur):
    # cur - for current coords y(h):x(w)
    global val
    y = cur[0]
    x = cur[1]
    m[y][x] = val
    val +=1
    if m[y-1][x] == path:
        go((y - 1, x))
    if m[y+1][x] == path:
        go((y + 1, x))
    if m[y][x+1] == path:
        go((y, x + 1))
    if m[y][x-1] == path:
        go((y, x - 1))

start_pos = (1, 1)
go(start_pos)

view()