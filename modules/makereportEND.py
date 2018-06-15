def makereportend(directory):
    reportfile = directory + '/report.html'
    with open(reportfile, 'a') as f:
        f.write('''
        </table>
        </center>
        </body>
        </html>''')
