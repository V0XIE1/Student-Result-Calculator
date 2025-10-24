#a CLI app that inputs marks, calculates total, average, and grade.
nosub=int(input('enter number of subjects:'))
total=0
for i in range(nosub):
    mark = int(input(f"Enter marks for subject {i+1}: ")) 
    total+=mark
avg=total/nosub
print('total marks:',total)
print('average marks:',avg)
if avg>=90:
    print('grade=A')
elif avg>=80:
    print('grade=B')
elif avg>=70:
    print('grade=C')
else:
    print('grade=D')

