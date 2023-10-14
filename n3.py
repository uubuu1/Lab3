my_f = open('n3.1', encoding='utf-8')
my_dict = {}
for line in my_f:
    hours = 0
    for i in range(1,len(line.split())):
        h = line.split()[i]
        while h[-1] not in ['1','2','3','4','5','6','7','8','9','0']:
            h = h[:len(h)-1]
        hours += int(h)
    print(hours)
    my_dict[line.split()[0]] = hours
print(my_dict)
my_f.close()