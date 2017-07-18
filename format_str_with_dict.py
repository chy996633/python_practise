template = '''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>%(title)s</title>
</head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>'''

data = {'title' : 'Welcome to Python Web', 'text' : 'This is the first page'}

print(template % data)

