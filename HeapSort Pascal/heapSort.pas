//Victor Sousa Firmino
//Engenharia de Computação
//Pesquisa e Ordenação
//Prof. Ronaldo Fernandes

program Heap_Sort;  
  
type Vetor = array of integer;  
var Vtamanho: integer;  
var V: Vetor;  
var i: integer;  
  

procedure trocaElementos ( var x, y: integer );  
var aux: integer;  
begin  
aux := x;  
x := y;  
y := aux;  
end;  
  

procedure trocaBaixo ( var V: Vetor; comecoVetor, fimVetor: integer );  
var raiz, filho: integer;  
begin  
raiz := comecoVetor;  
  

while ( raiz * 2 + 1 <= fimVetor ) do begin   
filho := raiz * 2 + 1; // left filho  
 
if ( filho < fimVetor ) and ( V[filho] < V[filho + 1] ) then  
filho := filho + 1; 
if ( V[raiz] < V[filho] ) then begin   
trocaElementos ( V[raiz], V[filho] );  
raiz := filho; 
end  
else  
break;  
end;  
end;  
  
procedure heapify ( var V: Vetor; contador: integer );  
var comecoVetor: integer;  
begin  

comecoVetor := (contador - 1) div 2;  
  
while ( comecoVetor >= 0 ) do begin  

trocaBaixo (V, comecoVetor, contador-1);  
comecoVetor := comecoVetor - 1;  

end;  
end;  
  
  
procedure heapSort( var V: Vetor; n: integer );  
var fimVetor: integer;  
begin  
 
heapify ( V, n );  
  
fimVetor := n - 1;  
while ( fimVetor > 0 ) do begin  
 
trocaElementos( V[fimVetor], V[0]);  

fimVetor := fimVetor - 1;  

trocaBaixo (V, 0, fimVetor);  
end;  
end;  
  
begin  
write ( 'Entre com o numero de elementos: ' );  
read ( Vtamanho );  

SetLength ( V, Vtamanho );  

randomize;  

for i := 0 to Vtamanho-1 do  
V[i] := random (100);  
  

for i := 0 to Vtamanho-1 do begin  
write (V[i]); write (' ');  
end;  
writeln;  
  
 
heapSort ( V, Vtamanho );  
  
 
for i := 0 to Vtamanho-1 do begin  
write (V[i]); write (' ');  
end;  
writeln;  
end.
