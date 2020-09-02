
bits = [0 0 0 0 0 1 0 1 1 0 1 0 1 1 0 1 1 1 1 0 1 1 0 0];
i = 1;
for j = 1:8
  b1 = bits(i);
  b2 = xor(bits(i), bits(i+1));
  b3 = xor(b2, bits(i+2)); 
  bi = [b1 b2 b3];
  d = bi(1)*4 + bi(2)*2 +bi(3)*1 +1
  i = i +3;
 end