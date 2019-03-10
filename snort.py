
#CCOID: hevyapan PYTHON Script to check each Snort CPU

import paramiko
import time
import re
import datetime
import csv

regex = r"(Id).*(Cpu-Usage).*Status\n.*sys\)\n.*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*"

#regex = r"(Id).*\n.*\n(\d).*(\s\d\d\d+\s).*\n(\d).*(\s\d\d\d\d+\s)"



hostname = "IP Address of FTD" #PUT THE IP ADDRESS OF FTD
username = "USERNAME" #USERNAME
password = "PASSWORD"#PASSWORD


remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(hostname, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)

time.sleep(2)
with open('snort_cpu.csv', mode='w') as csv_file:

    writer=csv.writer(csv_file)
    while True:
        time.sleep(1)
        remote_conn.send("show asp inspect-dp snort\n")
        output = remote_conn.recv(10000)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        id_cpu_pair={}
        temp_dict={}
        cpu_array = []
        id_array = []
        matches = re.finditer(regex,output, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1

                #print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,start=match.start(groupNum),end=match.end(groupNum),group=match.group(groupNum)))
                if groupNum != 1:
                    if groupNum !=2:
                        if groupNum % 2 != 0:
                            id_array.append(match.group(groupNum))
                        if groupNum % 2 == 0:
                            cpu_array.append(match.group(groupNum))

        for id in range(0, len(id_array)):

            temp_dict[id]=cpu_array[id]

        id_cpu_pair.update({st : temp_dict})

        cpu_time = id_cpu_pair.values()[0].keys()
        for cput in id_cpu_pair.keys():
            writer.writerow([cput] + [id_cpu_pair[cput][testtime] for testtime in cpu_time])








