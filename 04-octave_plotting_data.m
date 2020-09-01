t = [0:0.01:0.98]
y1 = sin(2*pi*4*t)
y2 = cos(2*pi*4*t)
%plot(t, y1)

hold on % con questa parola dico al programma di tenere i diversi plot insieme in un unica view
plot(t, y1, 'b')
plot(t, y2, 'r')
xlabel('time')
ylabel('value')
legend('sin', 'cos')
title('My Plot of SIN an COS')
print -dpng 'sincos.png'