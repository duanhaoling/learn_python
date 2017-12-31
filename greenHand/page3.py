# file = open('/Users/ldh/Desktop/file.txt','w')
# file.write('hello world!')

# 字符串的基本用法

what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Rebert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro, end=".\n")

print("\n* * * * * * * * * * * 字符串的基本用法 * * * * * * * * * * * * \n")

num = 1
string = '1'
# print(num + string)
print(type(num))
print(type(string))
words = "hi " * 3
print(words)

print("\n* * * * * * * * * * * NEXT * * * * * * * * * * * * \n")
word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)  # 等价于字符串'bang!'*4
print(total)

print("\n* * * * * * * * * * * 字符串的分片和索引 * * * * * * * * * * * * \n")
name = 'My Name is Mike'

print(name[0])
'M'
print(name[-4])
'M'
print(name[11:14])  # from 11th to 14th, 14th one is excluded
'Mik'
print(name[11:15])  # from 11th to 15th, 15th one is excluded
'Mike'
print(name[5:])
'me is Mike'
print(name[:5])
'My Na'
'hi hi hi hi'

word = 'friends'
find_the_evil_in_your_friends = word[0] + word[2:4] + word[-3:-1]
print(find_the_evil_in_your_friends)

url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]

print(file_name)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9], '*' * 9)
print(hiding_number)

print("\n* * * * * * * * * * * NEXT * * * * * * * * * * * * \n")

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search) + 1) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search) + 1) + ' to ' + str(num_b.find(search) + len(search)) + ' of num_b')

print("\n* * * * * * * * * * * 字符串格式化符 * * * * * * * * * * * * \n")

print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)