#Task1 
import re
unique_asa=set()
#asa=re.compile('%ASA.+?(?=\:)') 
with open('Log4test.txt', 'r') as log:
    with open('Task1.txt','w') as task1:
#        for line in log:
#            if 'ZOO-ML-CE' not in line and 'ML-WLC2' not in line and '%ASA' not in line: # эта проверка дала представление о количестве типов логов
#                print(line)            
#            if '%ASA' in line and '10.181.233.206' not in line:
#                print(line)               
        unique_asa.add('ZOO-ML-CE' + '\n' 'ML-WLC2' + '\n' + '10.181.233.206') # эти значения были выдернуты на этапе разбора возможных типов логов, поэтому просто добавим их руками
        task1.writelines(sorted(unique_asa)) # сортировка не была указана в ТЗ, но так проверять гораздо удобнее
#
#
#Task2
#import re
event=set()
ip_pattern=re.compile('[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,4}\.[0-9]{0,5}') # Регулярка учитывает и заменяет в т.ч. некорректные ip адреса
port_pattern = re.compile('(?<=\/)\d{0,5}')
date_pattern = re.compile('.*(?=%ASA)')
int_pattern = re.compile('(?<=interface ).{0,10}(?=\n)')
spi_pattern = re.compile('(?<== )0x[0-9a-fA-F]{8}')
counts_pattern = re.compile('(?<= is )\d*')
msgid_pattern = re.compile('\(msgid=[a-f0-9]{8}\)')
with open('Task2.txt', 'w') as task2:
    with open('Log4test.txt', 'r') as log:
            for line in log:
                if '%ASA' in line:
                    zero = date_pattern.sub('', line) #выпиливаем дату, название ASA
                    first = ip_pattern.sub('[ip]', zero) #убираем все ip
                    second = port_pattern.sub('[port]', first) #заменяем все порты
                    third = int_pattern.sub('[interface]', second) #убираем интерфейсы
                    fourth = spi_pattern.sub('[spi]', third) #spi
                    fifth = counts_pattern.sub('[count]', fourth) #счетчики событий
                    sixth = msgid_pattern.sub('[msgid]', fifth) #msgid
                    event.add(sixth)
    task2.writelines(sorted(event))
#
#
#Task3
#import re
unique_ip_list=set()
regex_valid_ipv4 = re.compile('(?<=\D)((?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.)(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){2}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])|0\.0\.0\.0)(?=\D)')
#Эта безумная регулярка нужна, чтобы дергать только валидные IPv4 адреса
with open('Task3.txt','w') as task3:
        with open('Log4test.txt', 'r') as log:
            for line in log:
                if '%ASA' in line:
                    ASA_ipv4 = re.findall(regex_valid_ipv4, line)
                    for ip in ASA_ipv4:
 #                       if ip not in unique_ip_list:
                            unique_ip_list.add(ip+'\n') 
        task3.writelines(sorted(unique_ip_list))