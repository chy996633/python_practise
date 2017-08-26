#pracise 8
formatter="%r %r %r %r"

print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)
print formatter %(
    "I had this thing.", #少打了一个this
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#A2：输入的是字符串，所以要用“”，但是输出的是元组，所以就是单引号啦
