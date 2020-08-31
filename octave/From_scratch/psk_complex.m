
%SNR range
snrlen=10;

%SNR in dB and actual per bit 
%(Check Proakis for factor of 6)
snr_db = linspace(0,snrlen,snrlen);
snr = 6.*10.^(0.1.*snr_db);

%Bitstream size
bitsimlen = 99999;

%Symbol stream size
simlen = bitsimlen / 3;

%Generating bits
bits = randi([0,1],1,bitsimlen);


s = zeros(8,2);
for i = 1:8
	s(i,:) = [cos((i-1)*2*pi/8)  sin((i-1)*2*pi/8)];
end
% Converting bits into gray code
symbol_lst=symb(bits,simlen,s);
symbol=symbol_lst.';
symbol_comp = symbol(1,:) + 1i*symbol(2,:);

ser=zeros(1,snrlen);
ser_anal=zeros(1,snrlen);
ber=zeros(1,snrlen);

gray = zeros(8,3);
gray(1,:) = [0 0 0];
gray(2,:) = [0 0 1];
gray(3,:) = [0 1 1];
gray(4,:) = [0 1 0];
gray(5,:) = [1 1 0];
gray(6,:) = [1 1 1];
gray(7,:) = [1 0 1];
gray(8,:) = [1 0 0];

  
A= zeros(8,2,2);
A(1,:,:) = [sqrt(2)-1 sqrt(2)-1; 1 -1];
A(2,:,:) = [sqrt(2)+1 -sqrt(2)+1;-1 1];
A(3,:,:) = [-sqrt(2)-1 sqrt(2)+1;1 1];
A(4,:,:) = [sqrt(2)-1 -sqrt(2)-1; 1 -1];
A(5,:,:) = [-sqrt(2)+1 -sqrt(2)+1;-1  1];
A(6,:,:) = [-sqrt(2)-1 sqrt(2)-1;1 -1];
A(7,:,:) = [sqrt(2)+1  -sqrt(2)-1;-1 -1];
A(8,:,:) = [-sqrt(2)+1 sqrt(2)+1;-1  1];

for k = 1:snrlen
    %noise = randn(2,simlen);
    noise_comp = randn(1,simlen) + 1i*randn(1,simlen);
    y_comp = sqrt(snr(k)).* symbol_comp + noise_comp;
    t=0;
    brx=zeros(simlen,3);
    for i=1:simlen
        z=decodecomp(y_comp(i),A);
        srx_comp=s(z,:);
        brx(i,:)= gray(z,:);
        
        if and(real(symbol_comp(i))== srx_comp(1,1), imag(symbol_comp(i))==srx_comp(1,2))
            t=t+1;
        end
    end
    disp(t);
    ser(k)= 1-(t/simlen);
    disp(ser(k));
    ser_anal(k) = 2*qfunc(sqrt(snr(k))*sin(pi/8));
    brx=brx.';
    brx = reshape(brx,[1,bitsimlen]);
    bit_diff = bits-brx;
    ber(k) = nnz(bit_diff)/bitsimlen; 
    
    
end

save ("-ascii", "psk.dat","snr_db","ser_anal","ser","ber");
%Plots
close all; figure
semilogy(snr_db,ser_anal,'o')
hold on
semilogy(snr_db,ser,'r')
hold on
semilogy(snr_db,ber,'b')
hold on
%axis([0 10 0.4 2.5])
grid on
xlabel('SNR in dB')
ylabel('Error Rate')
legend('SER Analysis','SER Simulation','BER Simulation')
title('BER & SER curve for 8PSK')





	