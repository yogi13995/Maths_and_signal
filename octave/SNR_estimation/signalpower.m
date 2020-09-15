function y = signalpower(x,l,p)
  for j = 1:l
    disp(x(j))
    disp(abs(x(j))^2)
     p = p + abs(x(j))^2
     
  y= p;
  end
end
