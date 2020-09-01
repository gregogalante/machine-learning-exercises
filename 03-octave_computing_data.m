A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16]
C = [1 1; 2 2]

% Moltiplicazione tra matrici
A * C

% Moltiplicazione valore per valore delle due matrici:
% Ogni elemento di A viene moltiplicato per il corrispondente (di posizione) in B
A .* B

% Elevazione dei valori di A:
% Ogni valore di A viene elevato al quadrato
A .^ 2

% Ottenimento valore massimo di una matrice
max(A)

% Ottenimento valore massimo di una matrice e indice
[val, ind] = max(A)