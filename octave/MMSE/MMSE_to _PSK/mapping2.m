function y =mapping2(bits, simlen)
%M=8;
i = 1;
for j = 1:simlen
  b1 = bits(i);
  b2 = xor(bits(i), bits(i+1));
  b3 = xor(b2, bits(i+2)); 
  bi = [b1 b2 b3];
  d = bi(1)*4 + bi(2)*2 +bi(3)*1 +1;
   
    I=cos((d-1)*2*pi/8);
    Q=sin((d-1)*2*pi/8);
    y1(1, j) = I+1i*Q;
    i=i+3;
end
y = y1;
end
