function y = symb(bits,simlen,s)
i=1;
symbol=zeros(1,simlen);
for k=1:simlen
    map=mapping2(s,bits(k,1),bits(k,2),bits(k,3));
    symbol(1,k)=map;
    i=i+1;
end
y=symbol;
end