# word = input("문자열: ")
# size = len(word)
#
# for i in range(1, size+1):
#     print(word[:i])
# for i in range(1, size+1):
#     print(word[:-i])

# word = ["welcome", "to", "the", "software", "world"]
# result = [ i[0].upper() for i in word ]
# print(result)

# s = "      hello,    world!!!    "
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s = "welcome to the python world"
# print(s.split())
#
# s = "hello, my good, friend"
# print(s.split(','))

s = " this, is,      my,      friend,     python"
data = s.split(",")
print([i.strip() for i in data])