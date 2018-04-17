def hello(fn):
    def wrapper():
        print "Hello, %s" % fn.__name__
        fn()
        print "Goodbye, %s" % fn.__name__
    return wrapper




@hello
def Samuel():
    print "I am Chenhaiyue"


Samuel()


def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds['css_class']) if 'css_class' in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">"+fn() + "</"+tag+">"
        return wrapped
    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="input", css_class="leftpadding10")
def hello():
    return "hello decorator"


print hello()
