#function h_hat = Channel_estimatiom(x_p,y_p,L)
function h_hat = channel_Estimation_fft(x_p,y_p,L)
    scaling_factor = 10e6;
    z_p = flip(y_p);
    y_p(1:L-1) = y_p(1:L-1)+flip(z_p(1:L-1));
    y = y_p(1:end-L+1);
    X = fft(x_p);
    Y = floor(fft(y)*scaling_factor);
    %disp(size(X));
    %disp(size(Y));
    H = Y./X;
    h_hat = ifft(H);

%     xc = x;
%     xr = [x(1) zeros(1,L-1)];
%     X = toeplitz(xc,xr);
%     h_hat = (X'*X)\X'*y;
end
