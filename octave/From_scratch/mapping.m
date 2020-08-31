function y = mapping(b0,b1,b2,s)
    if b0==0 && b1==0 && b2==0
        y=s(1,:);
    elseif b0==0 && b1==0 && b2==1
        y=s(2,:);
    elseif b0== 0 && b1==1 && b2== 1
        y= s(3,:);
    elseif b0== 0 && b1== 1 && b2== 0
		y= s(4,:);
    elseif b0== 1 && b1== 1 && b2== 0
		y= s(5,:);
    elseif b0==1 && b1== 1 && b2== 1
		y= s(6,:);
    elseif b0==1 && b1== 0 && b2== 1
		y =s(7,:);
    elseif b0==1 && b1== 0 && b2== 0
		y= s(8,:);
    end
    
end