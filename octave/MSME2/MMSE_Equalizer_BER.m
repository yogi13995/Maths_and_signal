clc;
clear;
close all;

TimeSlot=2e-3; %Transmit time duration
SNR = 1; %Signal to noise ratio
Rs = 123e3; % symbol rate %53.34
%scaling_factor = 10e6;
M=8;
%Nf = 5; % MMSE filter length
L = 5 ; % Channel filter length
%N = 1e4;   % Number of symbols
EbN0dB=0:1:15;  % SNR in dB
kk=log2(M);   
EsN0dB=EbN0dB+10*log10(kk);   % Adding 3 dB to SNR as we are calculating Symbol Error Rate

nFrames = 100;
len_frame = 500;
len_pilot1 = 3*10;
len_pilot=(len_pilot1/3);
len_seq1=3*4;
len_seq = (len_seq1/3);
N = (len_frame)*nFrames;


DataSym = randi([0 1],len_pilot1,1);
DataSym1=reshape(DataSym,3,[]);
DataSym2=transpose(DataSym1);

DataSym3=zeros(1,len_pilot);
for ii=1:(len_pilot)
    DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1;
end

pilot_sym = mapping(M,DataSym3');   % 8-PSK modulation
% %nErr_seq = zeros(1,length(EsN0dB));
SER_MMSE=zeros(1,length(EsN0dB));
 

for i=1:length(EsN0dB)
     nErr_mmse = 0;
     EsN01in=10.^(EsN0dB(i)/10);
     for j = 1:nFrames
         h1 = randn(L-1,1);
         h2 = randn(L-1,1);
         h  = h1 + 1i*h2;
         h = h/sqrt(2);
         h = [1; h] ;   % Rician fading channel
         h = h/sqrt(L);
          
         % Channel estimation
         Rk_p = conv(h,pilot_sym);
         noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
         noise=noiseSigma*(randn(length(Rk_p),1)+1i*randn(length(Rk_p),1));
         %noise=0+0j;
         %pilot = [pilot_sym(end-L+1:end);pilot_sym];
         y_p = Rk_p + noise;
         h_hat = channel_Estimation_fft(pilot_sym,y_p,L);
         h_est = h_hat(1:L);
         w = MMSE_matrix(h_est,length(h)+len_seq-1,EsN01in);
         for k=1:len_frame/len_seq  
             DataSym = randi([0 1],len_seq1,1);
             DataSym1=reshape(DataSym,3,[]);
             DataSym2=transpose(DataSym1);
             DataSym3=zeros(len_seq,1);

             for ii=1:(len_seq)
                 DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1;
             end
             m_psk = mapping(M,DataSym3'); 
             Rk = conv(h,m_psk);
             %Rk=m_psk;
             noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
             noise=noiseSigma*(randn(length(Rk),1)+1i*randn(length(Rk),1));
             %noise=0+0j;
             y=Rk+noise;   % Received symbols with AWGN noise
% 
%             % MMSE Equalizer
             x_hat = w*y;
             %x_hat=y;
%             %disp(size(dataSym));
%             % disp(size(x_hat))
             x_hat1=demapping(M,x_hat);
             x_hat2=(x_hat1-1);
             x_hat3=de2bi(x_hat2,3,'left-msb');
             x_hat4=transpose(x_hat3);
             x_hat5=reshape(x_hat4,[],1);
             
             nErr_mmse = nErr_mmse + sum(DataSym~=x_hat5);
         end
     end
    
     SER_MMSE(i) = nErr_mmse/(kk*N)
 end
%SER_MLSE_50 = sum(nErr_seq)/N     % Probability of error
% %% Theory with AWGN for 8-PSK modulation
% 
 EbN0=10.^(EbN0dB/10);
 theoreticalSER=(1/kk)*(erfc(sqrt(EbN0*log2(M))*sin(pi/M)));
 theory_bpsk = 1.0/2* erfc(sqrt(EbN0));

 
%% Plots
semilogy(EbN0dB,(SER_MMSE),'m-*');
hold on;

semilogy(EbN0dB,theoreticalSER,'r-*');
hold on;

semilogy(EbN0dB,theory_bpsk,'b-*');
hold on;

legend('MMSE','TheoryBER','TheoryBPSK','location','best');
xlabel('$\frac{E_s}{N_0}$(dB)','Interpreter','latex');
ylabel('$P_e$','Interpreter','latex');
%saveas(gcf,'Equalizers','eps');
grid on;
