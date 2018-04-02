#include <iostream>

using namespace std;

class Album{
public:
  void CompraSobre(int n_en_sobre);
  Album(int n);
  
private:
  int n_total;
  int n_repetidas;
  int n_en_album;
  
  int *album;
  int *repetidas;
};

void Album::CompraSobre(int n_en_sobre){
  int * sobre;
  sobre = new int[n_en_sobre];
  cout << n_en_sobre << " "<< n_total<< endl;
  //  delete [] sobre;
}

Album::Album(int n){
  cout << "Creando el album" << endl;
  album = new int[n];
  repetidas = new int[n];
  n_total = n;
  n_repetidas = 0;
  n_en_album = 0 ;
  for (int i=0;i<n_total;i++){
    album[i] = 0;
    repetidas[i] = 0;
  }
}

int main(){
  Album A(120);
  A.CompraSobre(5);
  //  A.CompraSobre(5);
}
