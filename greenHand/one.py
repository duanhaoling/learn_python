def text_create(name, msg):
    desktop_path = '/Users/ldh/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


# text_create('hello', 'hello world')


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


# text_filter('Python is lame!')  # 调用函数

def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)

# censored_text_create('Try', 'lame!lame!lame!')

for num in range(1, 11):  # 不包含11，因此实际范围是1～10
    print(str(num) + ' + 1 =', num + 1)
for i in range(1, 10):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i * j))