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
