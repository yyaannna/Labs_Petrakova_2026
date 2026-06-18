import cgi

print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()

n = int(form.getvalue("n"))
m = int(form.getvalue("m"))

A = []
B = []

for i in range(n):
    row = []

    for j in range(m):
        row.append(int(form.getvalue(f"a{i}{j}")))

    A.append(row)

for i in range(n):
    row = []

    for j in range(m):
        row.append(int(form.getvalue(f"b{i}{j}")))

    B.append(row)

C = []

for i in range(n):

    row = []

    for j in range(m):

        s = 0

        for k in range(m):
            s += A[i][k] * B[k][j]

        row.append(s)

    C.append(row)

print("""
<html>
<body>

<h2>Перша матриця</h2>
""")

for row in A:
    print(row, "<br>")

print("<h2>Друга матриця</h2>")

for row in B:
    print(row, "<br>")

print("<h2>Результат множення</h2>")

for row in C:
    print(row, "<br>")

print("""
</body>
</html>
""")