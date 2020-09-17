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
%NO of rampbits
Rampbits = 42;
Rampsymblen = 42/3;
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
DataSym20 = randi([0 1],UsedPilotBitsLen*5,1);
%Pilot Symbol Stream Used for channel Estimation
DataSym1=reshape(DataSym20,3,[]);
DataSym2=transpose(DataSym1);


s = PSKGen();
gray = zeros(8,3);
gray = graycode(); 
A= DemodMatrix();

pilot_sym = transpose(symb(DataSym2,length(DataSym2),s));   % 8-PSK modulation
rampsym2 = zeros(14,3);
rampsym0= transpose(symb(rampsym2,length(rampsym2),s));
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
         h_est = 0; 
         s_p =  0;
         h_est_N = 0;
         s_N = 0;
         
         %noise power

        for l = 1:14
          rampsym = rampsym0(l);
          Rk_pN = conv(h,rampsym);
          noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
          noise=noiseSigma*(randn(length(Rk_pN),1)+1i*randn(length(Rk_pN),1));
          y_pN =  noise;
          s_N = s_N + norm(y_pN)^2;
         end
          s_Navg = s_N/14
         % Channel estimation
         for k = 1:5
              pilot_sym1 = pilot_sym((kk-1)*10+1:(kk-1)*10+10);
              Rk_p = conv(h,pilot_sym1);
              noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
              noise=noiseSigma*(randn(length(Rk_p),1)+1i*randn(length(Rk_p),1));
              y_p = Rk_p + noise;
              h_hat = channel_Estimation_fft(pilot_sym1,y_p,ChannelFilterLen);
              h_est = h_est + h_hat(1:ChannelFilterLen);
              s_p = s_p + norm(h_hat)^2;
         end
         s_pavg = s_p/(50*10e12)
         SNR_est = 10*log10(s_pavg/s_Navg)
         disp(EbN0dB(i));
         h_est_av = h_est/5;
         w = MMSE_matrix(h_est_av,length(h)+ChannelEstSymbols-1,EsN01in);
       end
 end