function w = MMSE_matrix(h,l,snr)
    hr=[h(1); zeros(l-length(h),1)];
    hc=[h;zeros(l-length(h),1)];
    H=toeplitz(hc,hr);
%     disp(size(hr));
%     disp(size(hc));
%     disp(size(H));
%     disp(size(H'*H));
    w = inv((H'*H+ eye(size(H'*H))./snr))*H';
    %disp(size(w));
end
