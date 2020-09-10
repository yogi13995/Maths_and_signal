function m_psk=mapping(M,dataSym)
%M=8;
    I=cos((dataSym-1)/M*2*pi);
    Q=sin((dataSym-1)/M*2*pi);
    m_psk=(I+1i*Q);
end
