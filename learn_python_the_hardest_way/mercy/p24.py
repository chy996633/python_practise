#encoding:utf-8
#practice 24
print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\that do \n newlines and \t tabs.'

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five=10-2+3-6
print "This should be five:%s" %five

def secret_formula(started):
	jelly_beans=started*500
	jars=jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates  #这里如果不返回值，那下面的就算不出来了
	pass

start_point=10000
beans,jars,crates=secret_formula(start_point)  #首先调用函数，然后把算出来的值分别赋给b、j、c

print"With a starting point of:%d"%start_point
print"We'd have %d beans,%d jars,and %d crates."%(beans,jars,crates)

start_point=start_point/10

print"We can also do that this way:"
print"We'd have %d beans,%d jars,and %d crates."%secret_formula(start_point) #两种方法调用函数，这种还更简洁
