"""
shadowing allows us to use the same name to map to multiple objects if each mapping is done in a different scope

"""

# global
name = 'tom'

def hello_name(name):
    # local
    print 'hello {}'.format(name)

print name
hello_name('john')

#shadowing can be avoided using parallel scoping that is separating the global and local scopes into functions.

def main():
    name = 'tom'
    print 'hello {}'.format(name)

def hello_name(name):
    print 'hello {}'.format(name)

main()
hello_name('john')
