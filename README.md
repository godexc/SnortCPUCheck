# SnortCPUCheck
A Crude Python Script to Check SnortCPUs

Requirements:

  -Python 2.7 +
  
  -Paramiko
  
  -Connectivity to the Firepower Threat Defense Device.
  
  -Change the hostname, username and password variables on the code

That the script has been created in order to track CPU utilization on a customer. 

regex = r"(Id).*(Cpu-Usage).*Status\n.*sys\)\n.*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*\n(\d\d).*(\s\d\d*%\s).*"

Regex above can be tweaked based on the cores (the amount of cores differ based on product) the part you need to add or delete is \n(\d\d).*(\s\d\d*%\s).* this will help you to select the new ID and new CPU Usage under the tot.

Since this is basically screen scraping output you are expecting might vary.

Sample output that the script works on:

test_str = ("> show asp inspect-dp snort\n"
            " \n"
            "SNORT Inspect Instance Status Info\n"
            " \n"
            "Id Pid       Cpu-Usage    Conns      Segs/Pkts  Status\n"
            "          tot (usr | sys)\n"
            "-- ----- ---------------- ---------- ---------- ----------\n"
            "0  17688  21% ( 21%|  0%)   3.9 K      0        READY\n"
            "1  17699  15% ( 15%|  0%)   4   K      2        READY\n"
            "2  17694  16% ( 16%|  0%)   4   K      0        READY\n"
            "3  17696  16% ( 16%|  0%)   4   K      0        READY\n"
            "4  17698  20% ( 19%|  0%)   3.9 K      1        READY\n"
            "5  17703  26% ( 25%|  0%)   4   K      0        READY\n"
            "6  17691  14% ( 14%|  0%)   4   K      0        READY\n"
            "7  17706  16% ( 16%|  0%)   4   K      0        READY\n"
            "8  17689  21% ( 21%|  0%)   4   K      0        READY\n"
            "9  17690  36% ( 35%|  0%)   4   K      2        READY\n"
            "10 17692  13% ( 13%|  0%)   4   K      0        READY\n"
            "11 17704  14% ( 13%|  0%)   4   K      2        READY\n"
            "12 17702  15% ( 14%|  0%)   3.9 K      0        READY\n"
            "13 17693  21% ( 21%|  0%)   3.9 K      0        READY\n"
            "14 17695  28% ( 28%|  0%)   4   K      0        READY\n"
            "15 17697  15% ( 15%|  0%)   4.1 K      0        READY\n"
            "16 17707  17% ( 17%|  0%)   4   K      0        READY\n"
            "17 17705  12% ( 12%|  0%)   3.9 K      0        READY\n"
            "18 17709  16% ( 15%|  0%)   4   K      0        READY\n"
            "19 17708  13% ( 13%|  0%)   4   K      0        READY\n"
            "20 17701  18% ( 18%|  0%)   3.9 K      0        READY\n"
            "21 17700  11% ( 11%|  0%)   3.9 K      0        READY\n"
            " \n"
            ">")
            
# Things to be aware of

- Regex MUST BE CHANGED according to the "show asp inspect-dp snort" output as the number of CPUs assigned Snort Engine varies based on platform.
