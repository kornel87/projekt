import requests
import json
import webbrowser

source = []
liczby = []

for i in range(8):
    source.append("")

with open("liczby.json", "r") as f_liczby:
    js = json.loads(f_liczby.read())
    liczby = js


for x in range(len(liczby)):
 r = requests.get("https://xkcd.com/{}/info.0.json".format(liczby[x]))
 resp = r.content
 resp_d = json.loads(resp)
 source[x] = resp_d['img']
 


html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="index.css">
</head>

<body>

<div class = "container"> 

<div class = "column">
<img src = '{}'/>
</div>

<div class = "column">
<img src = '{}'/>
</div>



<div class = "column">
<img src = '{}'/>
</div>
<div class = "column">
<img src = '{}'/>
</div>



<div class = "column">
<img src = '{}'/>
</div>
<div class = "column">
<img src = '{}'/>
</div>



<div class = "column">
<img src = '{}'/>
</div>
<div class = "column">
<img src = '{}'/>
</div>


</div>


</body>
</html>

""".format(source[0], source[1],source[2],source[3],source[4],source[5],source[6],source[7])

with open("index.html", "w") as f:
    f.write(html_content)
    f.close()


print("HTML Content Created")