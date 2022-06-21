import re
ASA=set()
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
                    ASA.add(sixth)
    task2.writelines(sorted(ASA))
