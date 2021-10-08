# ini penggunaan sep dan end buat mengisi di sela-sela kata dan buat kata jadi satu baris
print('aku','kamu','dia')
print('aku','kamu','dia',flush=False) # jika ingin di flush atau tidak
print('aku','kamu','dia',sep =' , ')
print('aku',end=' ')
print('kamu')
print("dia")
print('','kamu','',sep =' "" ')
print(' "" ','kamu',"''")
print(' "" ','kamu',' "" ')
x=15.55000
c=round(x,100)
print(x)
y="aku kau kua"
print(y)

#coba
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n",) #\n buat mengakhiri dan membuat baris baru
print("yey")

#latihan
print("Programming","Essentials","in",sep='***',end="...")
print("Python")

#pencermatan
print("The itsy bitsy spider\nclimbed up the waterspout.")
print("The itsy bitsy spider\\climbed up the waterspout.")
#fuungsi (\) adalah versi manual sep dan end 
print("apa aja" ,"mau mu")
print("The itsy bitsy spider\"climbed up\" the waterspout.")
print("The itsy bitsy spider\"climbed up\"\"\"\" the waterspout.")
print()
