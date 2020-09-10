function y = PSKGen()
s = zeros(8,2);
for i = 1:8
	s(i,:) = [cos((i-1)*2*pi/8)  sin((i-1)*2*pi/8)];
end
y= s;
end 