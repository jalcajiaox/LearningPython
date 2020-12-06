
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames=[]
for x in filenames:
	if x[-4:]==".hpp":
		w=x[0:len(x)-2]
		newfilenames.append(w)
	else:
		newfilenames.append(x)

		

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]