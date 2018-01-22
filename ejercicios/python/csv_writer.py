import csv
import sys

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow( ('Signo', 'Sorteo', 'Fecha') )
    for i in range(20):
        writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
finally:
    f.close()

print(open(sys.argv[1], 'rt').read())