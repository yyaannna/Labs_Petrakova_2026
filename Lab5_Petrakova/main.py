from db import DocumentDB
import json

db = DocumentDB()


def menu():
    print("""
===== JSON DB =====
1. add
2. delete id
3. update
4. find
5. aggregate
6. groupby
7. save
8. load
9. show all
0. exit
""")


while True:

    menu()
    cmd = input(">> ")

    try:

        if cmd == "1":
            data = input("JSON: ")
            db.add(json.loads(data))
            print("OK")

        elif cmd == "2":
            _id = int(input("id: "))
            db.delete_by_id(_id)

        elif cmd == "3":
            _id = int(input("id: "))
            field = input("field: ")
            value = input("value: ")
            db.update(_id, field, value)

        elif cmd == "4":
            field = input("field: ")
            op = input("op (=,>,<,>=,<=,in): ")
            value = input("value: ")

            result = db.find(field, op, value)
            print(result)

        elif cmd == "5":
            op = input("operation (sum,avg,min,max,count): ")
            field = input("field: ")

            print(db.aggregate(op, field))

        elif cmd == "6":
            field = input("field: ")
            print(db.groupby(field))

        elif cmd == "7":
            filename = input("file: ")
            db.save(filename)

        elif cmd == "8":
            filename = input("file: ")
            db.load(filename)

        elif cmd == "9":
            print(json.dumps(db.data, indent=2, ensure_ascii=False))

        elif cmd == "0":
            break

    except Exception as e:
        print("Помилка:", e)