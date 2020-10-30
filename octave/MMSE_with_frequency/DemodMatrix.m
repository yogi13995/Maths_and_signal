function y = DemodMatrix()
  A= zeros(8,2,2);
A(1,:,:) = [sqrt(2)-1 sqrt(2)-1; 1 -1];
A(2,:,:) = [sqrt(2)+1 -sqrt(2)+1;-1 1];
A(3,:,:) = [-sqrt(2)-1 sqrt(2)+1;1 1];
A(4,:,:) = [sqrt(2)-1 -sqrt(2)-1; 1 -1];
A(5,:,:) = [-sqrt(2)+1 -sqrt(2)+1;-1  1];
A(6,:,:) = [-sqrt(2)-1 sqrt(2)-1;1 -1];
A(7,:,:) = [sqrt(2)+1  -sqrt(2)-1;-1 -1];
A(8,:,:) = [-sqrt(2)+1 sqrt(2)+1;-1  1];
 y = A;
 end