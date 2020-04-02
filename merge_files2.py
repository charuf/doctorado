def get_values_from_file(path):
    f = open(path, "r")
    result = []
    for i in f.readlines():
        # hay 3 tipos de separaciones diferentes: 1, 2 y 4 espacios
        value = i.strip().replace(",", ".").replace("  ", " ").replace("    ", " ").split(" ")[1]
        # tras la transformacion se comprueba que no haya vacios
        if value != "":
            result.append(value)
    f.close()
    return result

# se recogen los valores de los ficheros
a = get_values_from_file("PlasStopLi.txt")
b = get_values_from_file("PlasStopLi2.txt")

tresult = []
# suponiendo que los dos ficheros tienen las mismas lineas (se ha cogido la longitud de a)
for i in range(0, len(a) - 1 , 1): 
    tresult.append(float(a[i]) + float(b[i]))

mf = open("SumStopLi.txt","w+")
# range no acepta float
for i in range(0, len(a) - 1, 1): 
    # se divide entre 10 y queda igual
    mf.write(str(i/10) + '\t' + str(tresult[i]))

mf.close()
