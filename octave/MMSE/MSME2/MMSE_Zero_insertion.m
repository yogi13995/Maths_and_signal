clc;
clear;
close all;
%Frame Duration
FrameDuration=2e-3; 
SNR = 1; %Signal to noise ratio
SymbolTxRate= 123e3; % symbol rate %53.34
%Constellation Size
ConstellationSize=8;
ChannelFilterLen = 5 ; % Channel filter length
EbN0dB=0:1:15;  % SNR in dB
%Bits per symbol (8PSK)
kk=log2(ConstellationSize);   
EsN0dB = EbN0dB+10*log10(kk);   % Adding 3 dB to SNR as we are calculating Symbol Error Rate

nFrame = 2000;
%No of bits per frame
PayloadBitsLen = 240*3;
%No of symbols per frame
PayloadSymbsLen  = (PayloadBitsLen /3);
%No of pilot bits/frame used for channel estimation
UsedPilotBitsLen = 3*10;
%No of pilot symbols/frame used for channel estimation
UsedPilotSymbsLen =(UsedPilotBitsLen/3);
%No of bits for channel estimation
channelEstBits=3*4;
%No of symbols for channel estimation
ChannelEstSymbols = (channelEstBits/3);
%Total symbols used for channel estimation
N = (PayloadSymbsLen )*nFrame/2;
% Pilot bitstream per frame used for channel estimation
DataSym = randi([0 1],UsedPilotBitsLen,1);
%Pilot Symbol Stream Used for channel Estimation
DataSym1=reshape(DataSym,3,[]);
DataSym2=transpose(DataSym1);
%integer pilot symbols per frame used for channel estimation (0,1..,7)
DataSym3=zeros(1,UsedPilotSymbsLen);

for ii=1:(UsedPilotSymbsLen)
    DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1;
end
pilot_sym = mapping(ConstellationSize,DataSym3');   % 8-PSK modulation

% 
% % %nErr_seq = zeros(1,length(EsN0dB));
SER_MMSE=zeros(1,length(EsN0dB));

for i=1:length(EsN0dB)
     nErr_mmse = 0;
     EsN01in=10.^(EsN0dB(i)/10);
     for j = 1:nFrame
         h1 = randn(ChannelFilterLen-1,1);
         h2 = randn(ChannelFilterLen-1,1);
         h  = h1 + 1i*h2;
         h = h/sqrt(2);
         h = [1; h] ;                 % Rician fading channel
         h = h/sqrt(ChannelFilterLen);
           
         % Channel estimation
         Rk_p = conv(h,pilot_sym);
         noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
         noise=noiseSigma*(randn(length(Rk_p),1)+1i*randn(length(Rk_p),1));
         y_p = Rk_p + noise;
         h_hat = channel_Estimation_fft(pilot_sym,y_p,ChannelFilterLen);
         h_est = h_hat(1:ChannelFilterLen);
         w = MMSE_matrix(h_est,length(h)+ChannelEstSymbols-1,EsN01in);
%          %for k=1:PayloadSymbsLen 
  
             DataSym = randi([0 1],(PayloadBitsLen /2),1);
             DataSym1=reshape(DataSym,3,[]);
             DataSym2=transpose(DataSym1);
             DataSym3=zeros((PayloadSymbsLen /2),1);

             for ii=1:(PayloadSymbsLen /2)
                 DataSym3(ii)=bi2de(DataSym2(ii,:),'left-msb')+1;
             end
             m_psk = mapping(ConstellationSize,DataSym3');
             m_psk1 = zero_padding(m_psk);
             Rk = conv(h,m_psk1);
             Rk1 = reshape(Rk,[244,1]);
             %Rk=m_psk;
             noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
             noise=noiseSigma*(randn(length(Rk),1)+1i*randn(length(Rk),1));
             %noise=0+0j;
             y = Rk1 + noise;   % Received symbols with AWGN noise
             
             % MMSE Equalizer
             X_hat = [];
             nErr_frame = 0;
             for jj = 1:(PayloadSymbsLen /8)
                 y1 = y((jj-1)*8+1:(jj-1)*8+8);
                 x_hat = w*y1;
                 x_hat1=demapping(ConstellationSize,x_hat);
                 x_hat2=(x_hat1-1);
                 x_hat3=de2bi(x_hat2,3,'left-msb');
                 x_hat4=transpose(x_hat3);
                 x_hat5=reshape(x_hat4,[],1);
                 X_hat = [X_hat;x_hat5];
               %  disp(size(X_hat))
                 %nErr_frame = nErr_frame + sum(DataSym((jj-1)*4*3+1:(jj-1)*4*3+12)~=x_hat5);
              end              
              nErr_mmse = nErr_mmse + sum(DataSym~=X_hat);
              %nErr_mmse = nErr_mmse + nErr_frame; 
% %          % end
       end
%       
%     % SER_MMSE(i) = nErr_mmse/(N)
      SER_MMSE(i) = nErr_mmse/(3*N)
   end
% % 
EbN0=10.^(EbN0dB/10);
 theoreticalSER=(1/kk)*(erfc(sqrt(EbN0*log2(ConstellationSize))*sin(pi/ConstellationSize)));
 theory_bpsk = 1.0/2* erfc(sqrt(EbN0));

%% Plots
semilogy(EbN0dB,(SER_MMSE),'m-*');
hold on;

% semilogy(EbN0dB,theoreticalSER,'r-*');
% hold on;
% 
% semilogy(EbN0dB,theory_bpsk,'b-*');
% hold on;

legend('MMSE','TheoryBER','TheoryBPSK','location','best');
xlabel('$\frac{E_s}{N_0}$(dB)','Interpreter','latex');
ylabel('$P_e$','Interpreter','latex');
%saveas(gcf,'Equalizers','eps');
grid on;
