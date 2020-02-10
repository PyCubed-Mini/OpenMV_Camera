clc
clear
close all

m = 16;
for i = 0:19
    for j = 0:14
        file_name = ['picture_out_',num2str(i),'_',num2str(j),'.png'];
        A(j*m+1:j*m+m, i*m+1:i*m+m,:) = imread(file_name);
    end
end

imwrite(A,'picture_out_recreated_by_tile.jpeg')