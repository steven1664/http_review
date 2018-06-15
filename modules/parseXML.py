from libnmap.parser import NmapParser

http_ports = ['80', '8000', '8080']
https_ports = ['443', '8443']

def parsexml(files1):
    http_hosts = []
    for file1 in files1:
        nmap_report = NmapParser.parse_fromfile(file1)
        for port in http_ports:
            list1 = [ a.address for a in nmap_report.hosts if (a.get_open_ports()) and int(port) in [b[0] for b in a.get_open_ports()] and 1 not in [b[0] for b in a.get_open_ports()] ]
            for host in list1:
                http_hosts.append('http://' + host + ':' + port)
        for port in https_ports:
            list1 = [ a.address for a in nmap_report.hosts if (a.get_open_ports()) and int(port) in [b[0] for b in a.get_open_ports()] and 1 not in [b[0] for b in a.get_open_ports()] ]
            for host in list1:
                http_hosts.append('https://' + host + ':' + port)

    return http_hosts
