import re
ML_WLC2=set()
ZOO_ML_CE=set()
part1_ML_WLC2=re.compile('\*\w{1,30}')
date_ML_WLC2=re.compile('\w{2,3} \d{1,2} \d{1,2}:\d{1,2}:\d{1,2}\.\d{0,3}:')
with open('Log4test.txt') as task2:
    for line in task2:
        if 'ML-WLC2' in line:
            part1 = re.findall(part1_ML_WLC2, line)
            part2 = re.findall
            print(part1)




