function y = PSKGen()
s = zeros(5,8,2);
Ts = 1e-7;
delf = 10e4;
for j = 1:5
for i = 1:8
	s(j,i,:) = [cos((2*pi*delf*(j-1)*Ts) + (i-1)*2*pi/8)  sin((2*pi*delf*(j-1)*Ts) + (i-1)*2*pi/8)];
end
y= s;
end 