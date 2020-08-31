function y = decodecomp(vec_comp,A)

vec=zeros(2,1);
vec(1,1)=real(vec_comp);
vec(2,1)=imag(vec_comp);
 for i = 1:8
     y1= [A(i,:,1);A(i,:,2)]*vec;
        if and(y1(1,1)>=0,y1(2,1)>=0)
             y = i;
         end
 end

end
