from Matrix import Matrix
from Sheet_original import Sheet

sheet_1 = Sheet(10,30)
sheet_1.updateValue(0,0,"7")
sheet_1.updateValue(1,0,"5")
sheet_1.updateValue(0,1,"=(3+4)*2")
sheet_1.updateValue(0,2,"=A1+B1")
sheet_1.updateValue(1,2,"=A1-B1")
sheet_1.updateValue(2,2,"=A1*B1")
sheet_1.updateValue(0,3,"=(A1+8)/A2")

sheet_1.updateValue(1,3, "=max(A1,A2)")
sheet_1.updateValue(1,0,'=AA1')
#def fun(*args, **kargs):


print(sheet_1)
