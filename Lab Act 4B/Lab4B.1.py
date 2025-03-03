A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("a. Number of elements in A ∪ B:", (len(A | B)))
print("b. Number of elements in B but not in A or C:", len(B - (A | C)))
print("i. Elements in ((C ∩ B) − A) ∪ (C − (B ∪ A)):", ((C & B) - A) | C - (B | A))
print("ii. Elements in A ∩ C:", A & C)
print("iii. Elements in (A ∩ B) but not in C ∪ (B ∩ C):", ((A & B) - C) | (B & C))
print("iv. Elements in (A ∩ C) but not in B:", (A & C) - B)
print("v. Elements in A ∩ B ∩ C:", A & B & C)
print("vi. Elements in B but not in A or C:", B - (A | C))