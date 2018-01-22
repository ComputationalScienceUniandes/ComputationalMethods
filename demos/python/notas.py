import sys


def load_data(filename):
    infile = open(filename, 'r')
    print("estoy leyendo %s"%(filename))
    l = infile.readlines()
    infile.close()
    return l

def process_data(lineas, select="ganador"):
    nuevas_lineas = []
    linea_pierde = ''
    linea_gana = ''
    for linea in lineas:
        if(linea[0]!='#'):
            ls = linea.split()
            nota1 = float(ls[3])
            nota2 = float(ls[4])
            nota3 = float(ls[5])        
            promedio = (nota1 + nota2 + nota3)/3.0
            if((promedio>=3.0) & (select=="ganador")):                
                linea_gana = "%s %s %s %f\n"%(ls[0], ls[1], ls[2], promedio)
                nuevas_lineas.append(linea_gana)
            elif((promedio<3.0) & (select=="perdedor")):
                linea_pierde = "%s %s %s %f\n"%(ls[0], ls[1], ls[2], promedio)                
                nuevas_lineas.append(linea_pierde)                
    return nuevas_lineas

def write_data(lineas, filename):
    outfile = open(filename, 'w')
    print("estoy escribiendo %s"%(filename))
    for line in lineas:
        outfile.write(line)
    outfile.close()


lineas = load_data(sys.argv[1])
nuevas_ganador = process_data(lineas,  select='ganador')
write_data(nuevas_ganador, 'ganadores.txt')

