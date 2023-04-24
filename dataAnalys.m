%%
clear
data = load("data.csv");

x_data = [];
y_data = [];
z_data = [];

for i = 0:(length(data) - 1)
    if(abs(data(i + 1)) < 10000)
        if(mod(i, 3) == 0)
            x_data = [x_data data(i + 1)];
        elseif(mod(i, 3) == 1)
            y_data = [y_data data(i + 1)];
        else
            z_data = [z_data data(i + 1)];
        end
    end
end

x = linspace(0, length(x_data), length(x_data));

[peaks, location] = findpeaks(x_data, "MinPeakHeight", 2);

figure(1);
plot(x, x_data);
hold on;
plot(x(location), peaks, 'o');


figure(2);
hold on;
grid on;
axis([-50 50 -4 5]);
for a = 1:length(location)
    
    testCut = [];

    for i = (location(a) - 15):(location(a) + 15)
        testCut = [testCut x_data(i)];
    end
    testCut = lowpass(testCut, 0.2);
    xNew = linspace(0, length(testCut), length(testCut));
    plot(xNew, testCut);
end;
    


    

