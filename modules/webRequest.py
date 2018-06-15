import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import subprocess


def takescreenshot(url, directory):
    directory2 = directory + '/screenshots/'
    if not os.path.exists(directory2):
        os.makedirs(directory2)
    print('Taking screenshot for: ' + url)
    url2 = url.replace('http://','').replace('https://','').replace('.','_')
    p = subprocess.Popen(['chromium-browser', '--headless', '--disable-gpu', '--window-size=1200,1000', '--hide-scrollbars', '--screenshot='+ directory2 + url2 + '.png', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #p = subprocess.Popen(['firefox', '--headless', '--window-size=1200,1000', '--screenshot='+ directory + '/' + url2 + '.png', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()


def webcheck(web_host, directory):
    reportfile = directory + '/report.html'

    try:
        r = requests.head(web_host, verify=False)

        if r.status_code != 404:
            url2 = web_host.replace('http://','').replace('https://','').replace('.','_')
            takescreenshot(web_host, directory)
            with open(reportfile, 'a') as f:
                f.write('''
                <tr>
                <td><a href="'''+web_host+'''" target="_blank">'''+web_host+'''</a></td>
                <td><img src="./screenshots/'''+url2+'''.png" height="600" width="800"></td>
                </tr>''')
    except Exception:
        pass
