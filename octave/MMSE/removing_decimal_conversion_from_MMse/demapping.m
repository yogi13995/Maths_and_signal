function y_ind=demapping(M,rx)
%M=8;
received=rx;
s_i=zeros(1,M);
s_q=zeros(1,M);
for i=1:1:M
    s_i(i)=cos((i-1)/M*2*pi);
    s_q(i)=sin((i-1)/M*2*pi);
end
    y_ind = zeros(1, length(rx));
    for iter = 1:length(rx)
        min_dist = intmax;
        min_dist_ind = 0;
        for iter2 = 1:M
            real_dist = (s_i(iter2) - real(rx(iter)))^2;
            imag_dist = (s_q(iter2)- imag(rx(iter)))^2;
            total_dist = real_dist + imag_dist;
            if(total_dist < min_dist)
                min_dist = total_dist;
                min_dist_ind = iter2;
            end
        end
        y_ind(iter) = min_dist_ind;
    end
end
