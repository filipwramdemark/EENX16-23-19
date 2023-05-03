%%
clear

testfile = "Tester2/test17.csv";
testfile2 = "Tester2/test35.csv";

data = load(testfile);
data2 = load(testfile2);

x_data = [];
z_data = [];
x_time = [];
z_time = [];

x_data2 = [];
z_data2 = [];
x_time2 = [];
z_time2 = [];

t0 = data(1, 2);
t02 = data2(1, 2);

for i = 0:(length(data) - 1)
    if(abs(data(i + 1)) < 10000000)
        if(mod(i, 2) == 0)
            x_data = [x_data data(i + 1, 1)];
            x_time = [x_time (data(i + 1, 2) - t0)];
        else
            z_data = [z_data data(i + 1, 1)];
            z_time = [z_time (data(i + 1, 2) - t0)];
        end
    end
end

for i = 0:(length(data2) - 1)
    if(abs(data2(i + 1)) < 10000000)
        if(mod(i, 2) == 0)
            x_data2 = [x_data2 data2(i + 1, 1)];
            x_time2 = [x_time2 (data2(i + 1, 2) - t02)];
        else
            z_data2 = [z_data2 data2(i + 1, 1)];
            z_time2 = [z_time2 (data2(i + 1, 2) - t02)];
        end
    end
end

[peaks, location] = findpeaks(x_data, "MinPeakHeight", 3.5);
[peaks2, location2] = findpeaks(x_data2, "MinPeakHeight", 3.5);

figure(1);
subplot(2, 1, 1);
plot(x_time, x_data);
title(testfile);
hold on;
plot(x_time(location), peaks, 'o');

subplot(2, 1, 2);
plot(x_time2, x_data2);
title(testfile2);
hold on;
plot(x_time2(location2), peaks2, 'o');


figure(2);
hold on;
grid on;
axis([-10 30 -4 5]);
subplot(1, 2, 1);
hold on;
grid on;
title(testfile);

curveFit = [];
curveFitTime = [];

for a = 1:length(location)
    
    testCut = [];

    for i = (location(a) - 8):(location(a) + 8)
        testCut = [testCut x_data(i)];
    end
    xNew = linspace(0, length(testCut), length(testCut));
    curveFitTime = [curveFitTime xNew];
    curveFit = [curveFit testCut];
    
    plot(xNew, testCut);
    

end

%plot(curveFitTime, curveFit, '.');
hold on;
p1 = polyfit(curveFitTime, curveFit, 6);
x1 = linspace(min(curveFitTime), max(curveFitTime), 1000);
y1 = polyval(p1, x1);
plot(x1, y1, 'r', "LineWidth", 3);
offset = 1.5;
plot(x1, y1 + offset, '--b', "LineWidth", 1.5);
plot(x1, y1 - offset, '--b', "LineWidth", 1.5);

count1 = 0;

for i = 1:length(curveFit)
    if(curveFit(i) < (polyval(p1, curveFitTime(i)) - offset))
        count1 = count1 + 1;
        plot(curveFitTime(i), curveFit(i), 'x', "MarkerSize", 5, "Linewidth", 1.5);
    elseif(curveFit(i) > (polyval(p1, curveFitTime(i)) + offset))
        count1 = count1 + 1;
        plot(curveFitTime(i), curveFit(i), 'x', "MarkerSize", 5, "Linewidth", 1.5);
    end
end

percentage1 = count1 ./ length(curveFit);

disp("Part 1 percentage: ");
disp(percentage1);



subplot(1, 2, 2);
hold on;
grid on;
title(testfile2);

curveFit = 0;
curveFitTime = 0;

for a = 1:length(location2)
    
    testCut = [];

    for i = (location2(a) - 8):(location2(a) + 8)
        testCut = [testCut x_data2(i)];
    end
    xNew = linspace(0, length(testCut), length(testCut));
    
    curveFitTime = [curveFitTime xNew];
    curveFit = [curveFit testCut];
    
    plot(xNew, testCut);
end

%plot(curveFitTime, curveFit, '.');
p2 = polyfit(curveFitTime, curveFit, 6);

x1 = linspace(min(curveFitTime), max(curveFitTime), 1000);
y1 = polyval(p2, x1);
plot(x1, y1, 'r', "LineWidth", 3);
hold on;

offset = 1.5;
plot(x1, y1 + offset, '--b', "LineWidth", 1.5);
plot(x1, y1 - offset, '--b', "LineWidth", 1.5);

count2 = 0;

for i = 1:length(curveFit)
    if(curveFit(i) < (polyval(p2, curveFitTime(i)) - offset))
        count2 = count2 + 1;
        plot(curveFitTime(i), curveFit(i), 'x', "MarkerSize", 5, "Linewidth", 1.5);
    elseif(curveFit(i) > (polyval(p2, curveFitTime(i)) + offset))
        count2 = count2 + 1;
        plot(curveFitTime(i), curveFit(i), 'x', "MarkerSize", 5, "Linewidth", 1.5);
    end
end

disp(count2);

percentage2 = count2 ./ length(curveFit);

disp("Part 2 percentage: ");
disp(percentage2);
    


    

