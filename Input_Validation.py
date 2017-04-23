# Creating a function that provides input validation

def validateInput(x):
    x = str(x)
    x = x.lower()
    x = x.split()
    return x



z = "ThIs Is SparTa"

print validateInput(z)