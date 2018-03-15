from sys import argv

script, filename = argv

print "We're going to rease %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Good-bye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm goin to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# This does the same job as the above but on one line, note all must be in the brackets as
# .write() can only take one argument.
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

print "Now, type the name of the file you just brought fourth."

spawn = raw_input("> ")

open_spawn = open(spawn)
print open_spawn.read()

open_spawn.close()
