#practice 6
x="There are %d types of people." %10
binary="binary"   #binary-������
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not)

print x
print y

print "I said:%r."%x
print"I also said:'%s'."%y   #Ϊʲô�����С�������һ��û�У�
hilarious=False  #hilarious-���ֵġ��ǳ������ġ�ϲ���Խ���
joke_evaluation="Isn't that joke so funny?!%r"  #evaluation-��������ֵ

print joke_evaluation%hilarious

w="This is the left side of```"
e="a string with a right side"

print w+e #+���������ַ���
