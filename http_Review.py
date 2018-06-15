#!/usr/bin/python3
from modules import *
import argparse
import sys
import threading


def reportrun(web_hosts):
    reportFolder = reportOUTPUT.makereportFolder()
    makereportSTART.makereportstart(reportFolder)
    threads = []
    for host in web_hosts:
        t = threading.Thread(target=webRequest.webcheck, args=(host, reportFolder), daemon=True)
        threads.append(t)
        t.start()
    for thread in threading.enumerate():
        if thread is not threading.currentThread():
            thread.join()
    makereportEND.makereportend(reportFolder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Provide a text file or files with a list of IPs", nargs="+")
    parser.add_argument("-g", "--gnmap", help="Provide a Nmap gnmap file or files to parse", nargs="+")
    parser.add_argument("-x", "--xml", help="Provide a Nmap XML file or files to parse", nargs="+")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    if args.xml:
        web_hosts = parseXML.parsexml(args.xml)
        reportrun(web_hosts)

    if args.gnmap:
        web_hosts = parseGNMAP.parsegnmap(args.gnmap)
        reportrun(web_hosts)

    if args.file:
        web_hosts = parseFILE.parsefile(args.file)
        reportrun(web_hosts)
