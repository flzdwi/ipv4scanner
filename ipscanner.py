import nmap
nmScan = nmap.PortScanner()

nmScan.scan('0.0.0.0-999.999.999.999', '80')

for host in nmScan.all_hosts():
     print('IPv4 Address : %s (%s)' % (host, nmScan[host].hostname()))
     print('Kondisi : %s' % nmScan[host].state())
     for proto in nmScan[host].all_protocols():
         print('----------')
         print('Protokol : %s' % proto)
         lport = nmScan[host][proto].keys()
         for port in lport:
             print ('Port : %s\tKondisi Port : %s' % (port, nmScan[host][proto][port]['state']))


