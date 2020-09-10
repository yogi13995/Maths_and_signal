function y = symb(datasym,simlen,s)
i=1;
symbol=zeros(1,simlen);
for k=1:simlen
    map=mapping3(s,datasym(i));
    symbol(1,k)=map;
    i=i+1;
end
y=symbol;
end