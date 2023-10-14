my_f = open('n4.1', encoding='utf-8')
av_p = 0
k = 0
my_dict = {}
average_profit = 0
count = 0
for line in my_f:
    profit = int(line.split()[2])-int(line.split()[3])
    if profit > 0:
        av_p += profit
        k += 1
    average_profit += profit
    count += 1
    my_dict[line.split()[0]] = profit
my_list = (my_dict, {'Средняя прибыль': float('{:.2f}'.format(average_profit/count))})
print('Средняя прибыль компаний составила', float('{:.2f}'.format(av_p/k)))
my_f.close()
import json
with open('n4.2.json','w',encoding='utf-8') as f_json:
    json.dump(my_list,f_json,sort_keys=True,indent=4,ensure_ascii=False)
with open('n4.2.json', encoding='utf-8') as f_json:
    print(f_json.read())