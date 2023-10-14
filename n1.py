out_f = open('n1.1', 'w')
while True:
    inp_line = str(input())
    if inp_line == '': break
    out_f.write(inp_line.__add__('\n'))
out_f.close()

my_f = open('n1.1')
out_f = open('n1.2', 'w')
for line in my_f:
    if len(line.split()) > 1:
        out_f.write(line)
my_f.close()
out_f.close()