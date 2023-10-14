my_f = open('n2.1', encoding='utf-8')
sr = 0.00
k = 0
for line in my_f:
    if float(line.split()[1]) > 9999.99:
        print(line.split()[0])
    sr += float(line.split()[1])
    k += 1
print("Средняя величина дохода составляет", float('{:.2f}'.format(sr/k)))