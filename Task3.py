import re
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