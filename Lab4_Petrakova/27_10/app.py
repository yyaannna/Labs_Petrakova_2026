from flask import Flask, request, render_template_string

app = Flask(__name__)

matrix1 = []
n = 0
m = 0


@app.route("/", methods=["GET", "POST"])
def index():

    html = """
    <h2>Введіть розміри матриць</h2>

    <form method="post">

        n:
        <input type="number" name="n" required>

        <br><br>

        m:
        <input type="number" name="m" required>

        <br><br>

        <input type="submit" value="Далі">

    </form>
    """

    if request.method == "POST":

        global n, m

        n = int(request.form["n"])
        m = int(request.form["m"])

        return matrix1_page()

    return html


def matrix1_page():

    html = """
    <h2>Перша матриця</h2>

    <form method="post" action="/matrix2">
    """

    for i in range(n):
        for j in range(m):

            html += f"""
            <input type="number"
                   name="a{i}{j}"
                   required>
            """

        html += "<br><br>"

    html += """
    <input type="submit" value="Далі">
    </form>
    """

    return html


@app.route("/matrix2", methods=["POST"])
def matrix2():

    global matrix1

    matrix1 = []

    for i in range(n):

        row = []

        for j in range(m):
            row.append(int(request.form[f"a{i}{j}"]))

        matrix1.append(row)

    html = """
    <h2>Друга матриця</h2>

    <form method="post" action="/result">
    """

    for i in range(n):
        for j in range(m):

            html += f"""
            <input type="number"
                   name="b{i}{j}"
                   required>
            """

        html += "<br><br>"

    html += """
    <input type="submit" value="Обчислити">
    </form>
    """

    return html


@app.route("/result", methods=["POST"])
def result():

    matrix2 = []

    for i in range(n):

        row = []

        for j in range(m):
            row.append(int(request.form[f"b{i}{j}"]))

        matrix2.append(row)

    # Множення
    result_matrix = []

    for i in range(n):

        row = []

        for j in range(m):

            s = 0

            for k in range(m):
                s += matrix1[i][k] * matrix2[k][j]

            row.append(s)

        result_matrix.append(row)

    return render_template_string("""
    <h2>Перша матриця</h2>
    {{A}}

    <h2>Друга матриця</h2>
    {{B}}

    <h2>Результат</h2>
    {{C}}
    """,
    A=matrix1,
    B=matrix2,
    C=result_matrix)


if __name__ == "__main__":
    app.run(debug=True)