from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening the file..."
# reading = r, write (and truncate) = w, reading and update = r+
target = open(filename, 'r+')

print "Here's the file content:"
print target.read()

print "truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

content = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(content)

print "And finally, we close it."
target.close()