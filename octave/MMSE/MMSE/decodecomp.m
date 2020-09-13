function y = decodecomp(rex,A,gray)

for j = 1:length(rex)
    vec=zeros(2,1);
    vec(1,1)=real(rex(j));
    vec(2,1)=imag(rex(j));
    for i = 1:8
        y1= [A(i,:,1);A(i,:,2)]*vec;
            if and(y1(1,1)>=0,y1(2,1)>=0)
                y2 = i;
            end
    end
 brx(j,:)= gray(y2,:);
end
y = brx;
end