function y = graycode()
gray = zeros(8,3);
gray(1,:) = [0 0 0];
gray(2,:) = [0 0 1];
gray(3,:) = [0 1 1];
gray(4,:) = [0 1 0];
gray(5,:) = [1 1 0];
gray(6,:) = [1 1 1];
gray(7,:) = [1 0 1];
gray(8,:) = [1 0 0];
 y = gray;
 end 