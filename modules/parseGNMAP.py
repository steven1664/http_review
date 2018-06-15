http_ports = ['80', '8000', '8080']
https_ports = ['443', '8443']

def parsegnmap(files1):
    http_hosts = []
    for file1 in files1:
        with open(file1, 'r') as f:
            for line in f:
                for port in http_ports:
                    checkport = ' ' + port + '/open/tcp//'
                    if checkport in line and '1/open/tcp//tcpmux' not in line:
                        lineout = line.split()
                        http_hosts.append('http://' + lineout[1] + ':' + port)
                for port in https_ports:
                    checkport = ' ' + port + '/open/tcp//'
                    if checkport in line and '1/open/tcp//tcpmux' not in line:
                        lineout = line.split()
                        http_hosts.append('https://' + lineout[1] + ':' + port)


    return http_hosts
