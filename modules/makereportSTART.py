def makereportstart(directory):
    reportfile = directory + '/report.html'
    with open(reportfile, 'w+') as f:
        f.write('''<!DOCTYPE html>
        <html>
        <head>
            <title>HTTP Review Report</title>
        </head>

        <body>
        <center>
            <h1>HTTP Review Report Output</h1>

        <table border = "1">''')
