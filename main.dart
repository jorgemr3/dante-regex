import 'dart:core';

void main(){

//TODO: LEER LA DOCUMENTACION!!!

final RegExp regex = RegExp(r'^[+-]?(?=\d+\.?\d*$|\.?\d+)(\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?$', multiLine: false);
final RegExp regex_2 = RegExp(r'^-[0-9]*\.[0-9]+$');
final RegExp regex_3 = RegExp(r'^\+[0-9]*\.[0-9]+$');

final String cadena = '1';

// no puede tener match con regex 2 y 3 porque excluyo especificamente los numeros positivos o 
//negativos que empiezan con un punto en su parte entera
// pero no tienen nada antes de el punto

// TODO : SI SIRVE

if(regex.hasMatch(cadena) && !regex_2.hasMatch(cadena) && !regex_3.hasMatch(cadena)){
  print('La cadena es un número valido ');
}
else{ print('La cadena no es valida'); }

}