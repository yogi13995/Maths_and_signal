function y = demapping(rx)

vec=zeros(2,1);
vec(1,1)=real(rx);
vec(2,1)=imag(rx);
for j=1:1:8
    s_i(j)=cos((j-1)/8*2*pi);
    s_q(j)=sin((j-1)/8*2*pi);
end
min_dist = intmax;
min_dist_ind = 0;
 for i = 1:8
     real_dist = (s_i(i) - real(rx))^2;
            imag_dist = (s_q(i)- imag(rx))^2;
            total_dist = real_dist + imag_dist;
            if(total_dist < min_dist)
                min_dist = total_dist;
                min_dist_ind = i;
            end
 end
y = min_dist_ind;
end