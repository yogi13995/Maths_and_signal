function y = mapping2(s,b0,b1,b2,j)
    if b0==0 && b1==0 && b2==0
        I=s(j,1,1);
        Q=s(j,1,2);
        y=(I+1i*Q);
    elseif b0==0 && b1==0 && b2==1
        I=s(j,2,1);
        Q=s(j,2,2);
        y=(I+1i*Q);
    elseif b0== 0 && b1==1 && b2== 0
        I=s(j,3,1);
        Q=s(j,3,2);
        y=(I+1i*Q);
    elseif b0== 0 && b1== 1 && b2== 1
		    I=s(j,4,1);
        Q=s(j,4,2);
        y=(I+1i*Q);
    elseif b0== 1 && b1== 0 && b2== 0
		    I=s(j,5,1);
        Q=s(j,5,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 0 && b2== 1
		    I=s(j,6,1);
        Q=s(j,6,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 1 && b2== 0
		    I=s(j,7,1);
        Q=s(j,7,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 1 && b2== 1
		    I=s(j,8,1);
        Q=s(j,8,2);
        y=(I+1i*Q);
    end  
end