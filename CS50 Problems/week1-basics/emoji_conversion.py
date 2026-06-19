def convert(text):
    return text.replace(':)', '🙂').replace(':(', '🙁')

def main():
    user_input = input()
    converted_faces = convert(user_input)
    print(converted_faces)

main()