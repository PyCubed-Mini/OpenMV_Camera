full_rgb = imread('picture_out_compression30_telephoto_1.jpeg');
R_matrix = full_rgb(:,:,1);
G_matrix = full_rgb(:,:,2);
B_matrix = full_rgb(:,:,3);

[U_R, S_R, V_R] = svd(single(R_matrix));
[U_G, S_G, V_G] = svd(single(G_matrix));
[U_B, S_B, V_B] = svd(single(B_matrix));

S_R_new = zeros(480, 640);
S_G_new = zeros(480, 640);
S_B_new = zeros(480, 640);

% if the singular value is less than 1% of the largest singular value, omit
for i = 1:480 
    if S_R(i,i) > S_R(1,1)*0.01
        S_R_new(i,i) = S_R(i,i);
    end
    if S_G(i,i) > S_G(1,1)*0.01
        S_G_new(i,i) = S_G(i,i);
    end
    if S_B(i,i) > S_B(1,1)*0.01
        S_B_new(i,i) = S_B(i,i);
    end
end

R_matrix_new = U_R*S_R_new*V_R';
G_matrix_new = U_G*S_G_new*V_G';
B_matrix_new = U_B*S_B_new*V_B';

full_rgb_new(:,:,1) = uint8(R_matrix_new);
full_rgb_new(:,:,2) = uint8(G_matrix_new);
full_rgb_new(:,:,3) = uint8(B_matrix_new);
imwrite(full_rgb_new,'picture_out_compression30_telephoto_1_recreated.jpeg')