from translate import Translator

translator = Translator(to_lang="ja")

print(translator)

try:
    with open('test.txt', 'r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your path silly!')
