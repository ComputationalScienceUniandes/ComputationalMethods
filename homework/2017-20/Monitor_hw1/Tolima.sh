mkdir DatosTolima && cd DatosTolima
cp ../DatosTolima.dat . && cp ../PlotsTolima.py .

sed 's/^\s/1/g' DatosTolima.dat | awk '{print $2, $5, $7}' | tail -n +2 > GRF_vs_EQ.txt

grep 'March' GRF_vs_EQ.txt > DatosMarzo.txt

python PlotsTolima.py
rm DatosTolima.dat
