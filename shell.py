from src.main import run

while True:
    text = input('pr >')
    result, error = run('<stdin>', text)

    if error:
        print(error)
    else:
        print(result)
