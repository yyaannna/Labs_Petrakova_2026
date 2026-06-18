import cgi

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

n = int(form.getvalue("n"))
m = int(form.getvalue("m"))

matrix1 = []

for i in range(n):
    row = []

    for j in range(m):
        row.append(form.getvalue(f"a{i}{j}"))

    matrix1.append(row)

print("""
<html>
<body>

<h2>Введіть другу матрицю</h2>

<form action="/cgi-bin/result.py" method="post">
""")

for i in range(n):
    for j in range(m):
        print(f"""
        <input type="text"
               name="b{i}{j}"
               size="3"
               required>
        """)
    print("<br><br>")

for i in range(n):
    for j in range(m):
        print(f"""
        <input type="hidden"
               name="a{i}{j}"
               value="{matrix1[i][j]}">
        """)

print(f"""
<input type="hidden" name="n" value="{n}">
<input type="hidden" name="m" value="{m}">

<input type="submit" value="Обчислити">

</form>

</body>
</html>
""")