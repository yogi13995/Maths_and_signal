bits = [0 0 0;0 0 1;0 1 1;0 1 0 ;1 1 0;1 1 1;1 0 1;1 0 0];

i=1;
symbol=zeros(1,8);
for k=1:8
    map=ex2(s,bits(k, 1),bits(k, 2),bits(k, 3));
    symbol(1,k)=map;
    i=i+1;
end
y=symbol;

