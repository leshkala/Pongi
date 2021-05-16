import pickle
favorite = ['a','s','d','c','n','q','h']
save_file = open('C:\\Users\\Alex\\Desktop\\favorites.dat', 'wb')
pickle.dump(favorite, save_file)
save_file.close()
load_file = open('C:\\Users\\Alex\\Desktop\\favorites.dat', 'rb')
loaded = pickle.load(load_file)
load_file.close()
print(loaded)