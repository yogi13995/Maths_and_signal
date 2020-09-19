function y = mapping2(s,b0,b1,b2)
    if b0==0 && b1==0 && b2==0
        I=s(1,1);
        Q=s(1,2);
        y=(I+1i*Q);
    elseif b0==0 && b1==0 && b2==1
        I=s(2,1);
        Q=s(2,2);
        y=(I+1i*Q);
    elseif b0== 0 && b1==1 && b2== 1
        I=s(3,1);
        Q=s(3,2);
        y=(I+1i*Q);
    elseif b0== 0 && b1== 1 && b2== 0
		    I=s(4,1);
        Q=s(4,2);
        y=(I+1i*Q);
    elseif b0== 1 && b1== 1 && b2== 0
		    I=s(5,1);
        Q=s(5,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 1 && b2== 1
		    I=s(6,1);
        Q=s(6,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 0 && b2== 1
		    I=s(7,1);
        Q=s(7,2);
        y=(I+1i*Q);
    elseif b0==1 && b1== 0 && b2== 0
		    I=s(8,1);
        Q=s(8,2);
        y=(I+1i*Q);
    end  
end