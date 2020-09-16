function y = zero_padding(x)
    y = [];
    for i = 1:(length(x)/4)
       y = [y x((i-1)*4+1:(i-1)*4+4) zeros(1,4)];  
    end
end

