import cgi

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

n = int(form.getvalue("n"))
m = int(form.getvalue("m"))

print(f"""
<html>
<body>

<h2>Введіть першу матрицю</h2>

<form action="/cgi-bin/matrix2.py" method="post">
""")

for i in range(n):
    for j in range(m):
        print(f"""
        <input type="text"
               name="a{i}{j}"
               size="3"
               required>
        """)
    print("<br><br>")

print(f"""
<input type="hidden" name="n" value="{n}">
<input type="hidden" name="m" value="{m}">

<input type="submit" value="Далі">

</form>

</body>
</html>
""")