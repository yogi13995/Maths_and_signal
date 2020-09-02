function y = symb(bits,simlen,s)
i=1;
symbol=zeros(simlen,2);
for k=1:simlen
    map=mapping(bits(i),bits(i+1),bits(i+2),s);
    symbol(k,:)=map;
    i=i+3;
end
y=symbol;