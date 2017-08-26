#practice 6
x="There are %d types of people." %10
binary="binary"   #binary-二进制
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not)

print x
print y

print "I said:%r."%x
print"I also said:'%s'."%y   #为什么这里有‘’上面一行没有？
hilarious=False  #hilarious-欢闹的、非常滑稽的、喜不自禁的
joke_evaluation="Isn't that joke so funny?!%r"  #evaluation-评估、求值

print joke_evaluation%hilarious

w="This is the left side of```"
e="a string with a right side"

print w+e #+连接两个字符串
