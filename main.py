#20.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество чисел, больших К в четных столбцах , чем произведение чисел в нечетных строках , то поменять местами С и Е симметрично, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
from random import randint as rnd
import numpy as np
import matplotlib.pyplot as plt

def printMtrx(mtrxA):
  for i in range(len(mtrxA)):
    for j in range(len(mtrxA[i])):
      print(mtrxA[i][j], end = " ")
    print()
  print("-------------")

k = int(input("Введите число K: "))
n = int(input("Введите число N: "))
m = n//2
n = m*2
A = []
for i in range(n):
  row = []
  for j in range(n):
    row.append(rnd(-10, 10))
  A.append(row)

print("Матрица A: ")
printMtrx(A)

b = []
c = []
d = []
e = []
for i in range(m):
  rowB = []
  rowC = []
  rowD = []
  rowE = []
  for j in range(m):
    rowB.append(A[i+m][j+m])
    rowC.append(A[i+m][j])
    rowD.append(A[i][j])
    rowE.append(A[i][j+m])
  b.append(rowB)
  c.append(rowC)
  d.append(rowD)
  e.append(rowE)
  
print("Подматрица D: ")
printMtrx(d)
print("Подматрица E: ")
printMtrx(e)
print("Подматрица C: ")
printMtrx(c)
print("Подматрица B: ")
printMtrx(b)

numsElem = 0
for i in range(len(e)):
  for j in range(len(e[i])):
    if (j+1) % 2 != 0: continue
    if e[i][j] > k: numsElem += 1

composNum = 1
for i in range(len(e)):
  if (i+1) % 2 == 0: continue
  for j in range(len(e[i])):
    composNum *= e[i][j]

if numsElem > composNum:
  print("Кол-во элементов в четных столбцах больше")
  for i in range(m):
    for j in range(m):
      c[i][j],e[i][m-j-1] = e[i][m-j-1], c[i][j]
if numsElem < composNum:
  print("Произведение элементов в нечетных строках больше")
  for i in range(m):
    for j in range(m):
      c[i][j],b[i][j] = b[i][j],c[i][j]

F = []
F.extend(d)
F.extend(c)
for i in range(m):
    F[i].extend(e[i])
for i in range(m, n):
    F[i].extend(b[i-m])

print("Матрица F : ")
printMtrx(F)

arrA = np.array(A)
arrF = np.array(F)
trasnposeA = arrA.transpose()
trasnposeF = arrF.transpose()

detA = np.linalg.det(arrA)
sumDiagF = 0
for i in range(len(F)):
    sumDiagF += F[i][i]

if detA > sumDiagF:#A*(At) - K*(F-1)
  print("Определитель А БОЛЬШЕ суммы диагональных элементов F")
  a1 = np.matmul(A, trasnposeA)
  print("A * At")
  printMtrx(list(a1))
  b1 = np.linalg.inv(arrF)
  b1 *= k
  print("K * F-1")
  printMtrx(list(b1))
  res = np.add(a1, (-1)*b1)
  print("A * At - K * F-1")
  printMtrx(list(res))
else: #((A-1)+G-(Ft))*K
  print("Определитель А МЕНЬШЕ суммы диагональных элементов F")
  a1 = np.linalg.inv(arrA)
  print("A-1")
  printMtrx(list(a1))
  g = np.tril(arrA, 0)
  print("G")
  printMtrx(list(g))
  b2 = np.add(a1, g)
  b2 = np.add(b2, (-1)*trasnposeF)
  b2 *= k
  print("(A-1 + G - Ft)*K")
  printMtrx(list(b2))

plt.title("Зависимости: y =sin от элементов F, x = соs от элементов F")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(np.cos(F),np.sin(F),linestyle="--",color="r")

plt.show()

plt.title("Высота столбца от числа элемента первой строки")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.bar(range(0,n),F[0],color='r',alpha=0.9)

plt.show()

plt.title("соответсвие номера и квадрата элемента из первой строки ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(range(0,n),F[0],linestyle="-",color="g")

plt.show()
