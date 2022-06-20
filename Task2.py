from asyncio import tasks
import re
ML_WLC2=set()
ZOO_ML_CE=set()
ASA=set()
'''
part1_ML_WLC2=re.compile('\*\w{1,30}')
part2_ML_WLC2=re.compile('(?<=#)+.*')
date_ML_WLC2=re.compile('\w{2,3} \d{1,2} \d{1,2}:\d{1,2}:\d{1,2}\.\d{0,3}:')
with open('Log4test.txt') as log:
    for line in log:
        if 'ML-WLC2' in line:
            part1 = re.findall(part1_ML_WLC2, line)
            part2 = re.findall(part2_ML_WLC2, line)
            for output in part1:
                for output2 in part2:
                    ML_WLC2.add(output+'\t'+output2+'\n') 
with open('task2.txt', "w") as task2:
        task2.writelines(sorted(ML_WLC2))
'''

'''
with open('Log4test.txt', 'r') as log:
    for line in log:
        if 'ZOO-ML-CE' in line and 'PFE_FW_SYSLOG_IP' not in line and '  A  ' not in line:
#Убеждаемся, что от источника событий ZOO-ML-CE падают только сообщения PFE_FW_SYSLOG_IP, action = accept и last message repeated X times
            print(line)
'''
ip_pattern=re.compile('[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,5}') # Регулярка учитывает и заменяет в т.ч. некорректные ip адреса
port_pattern = re.compile('(?<=\/)\d{0,5}')
date_pattern = re.compile('.*ASA-[0-9]-[0-9]{6}: ')
int_pattern = re.compile('(?<=interface ).{0,10}(?=\n)')
with open('tast2.txt', 'w') as task2:
    with open('Log4test.txt', 'r') as log:
            for line in log:
                if '%ASA' in line:
                    zero = date_pattern.sub('', line)
                    first = ip_pattern.sub('[ip]', zero)
                    second = port_pattern.sub('[port]', first)
                    third = int_pattern.sub('', second)
                  #  print(third)
                    ASA.add(third)
    task2.writelines(sorted(ASA))
#Отсекаем дату, имя узла (?<=ASA-[0-9]-[0-9]{6}: )\w.*
#Заменяем ip [0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,5}
#Заменяем порт (?<=\/)\d{0,5}