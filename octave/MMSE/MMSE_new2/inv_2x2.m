function P_inv = inv_2x2(P)
    det = P(1,1)*P(2,2)-P(1,2)*P(2,1);
    P_inv = [P(2,2),-P(1,2);-P(2,1),P(1,1)]./det;
end

