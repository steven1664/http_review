def parsefile(files1):
    http_hosts = []
    for file1 in files1:
        with open(file1, 'r') as f:
            for line in f:
                http_hosts.append(line.rstrip())

    return http_hosts
