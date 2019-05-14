try:
    print(x)
except Exception as a:
    print "Exception occurred: ", a
finally:
    print("done")

print()

try:
    print(x)
except NameError:
    print("Variable not defined")
except:
    print("Some error occurred")
else:
    print("Everything went good")
finally:
    print("done")
