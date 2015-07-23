### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[3] #第一位是s[0]
print s1[0:7] 
#输出Rixner'[0:7]表示输出s[0]到s[6]的字符，不包括s[7]
print len(s1) 
#输出s1的字符个数
print s2[6:] 
#输出从s[6]以后的字符，直到结束。包括s[6]
print s1[0:6] + s2[6:] 
print s2[:13] + s1[9:] + s3
#s2[:13]表示从开头开始一直到s2[13],但不包括s[13]

# Converting strings
s5 = str(375)
#将整形375强制转换成str类型
print s5[1:]
i1 = int(s5[1:])
#把s5[1:]这个字符串强制转变成int型
print i1 + 38
