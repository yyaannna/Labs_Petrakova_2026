from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Зміна знаків</title>
</head>
<body>

<h2>Введіть послідовність чисел</h2>

<form method="post">

    <input type="text"
           name="numbers"
           size="50"
           placeholder="Наприклад: 1 -34 8 14 -5 0">

    <br><br>

    <input type="submit" value="Обробити">

</form>

{% if result is not none %}
    <h3>Кількість змін знаку: {{ result }}</h3>
{% endif %}

{% if error %}
    <h3 style="color:red">{{ error }}</h3>
{% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():

    result = None
    error = ""

    if request.method == "POST":

        try:
            data = request.form["numbers"]

            numbers = list(map(int, data.split()))

            if numbers[-1] != 0:
                raise ValueError

            sign_changes = 0

            for i in range(len(numbers) - 2):

                if numbers[i] * numbers[i + 1] < 0:
                    sign_changes += 1

            result = sign_changes

        except:
            error = "Помилка введення даних"

    return render_template_string(
        HTML,
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)