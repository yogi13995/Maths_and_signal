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