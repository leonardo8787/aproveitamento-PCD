% Frequência de amostragem do sinal
Fs = 40000;

% Período de amostragem do sinal
Ts = 1 / Fs;

% Variável tempo amostrada
t = 0:Ts:2-Ts;

% Sinal modulante de frequência angular de 1000 rad/s
m = cos(1000 * t);

% Sinal da portadora
p = cos(10000 * t);

% Sinal modulado
x = m .* p;

% Plotagem dos gráficos com zoom
figure;

subplot(3,1,1);
plot(t, m, 'b', 'LineWidth', 1);
xlabel('t');
ylabel('m(t)');
title('Sinal Modulante');
xlim([0 0.01]); % Zoom no eixo x
ylim([-1.5 1.5]); % Ajuste no eixo y

subplot(3,1,2);
plot(t, p, 'y', 'LineWidth', 1);
xlabel('t');
ylabel('p(t)');
title('Sinal da Portadora');
xlim([0 0.01]); % Zoom no eixo x
ylim([-1.5 1.5]); % Ajuste no eixo y

subplot(3,1,3);
plot(t, x, 'g', 'LineWidth', 1);
xlabel('t');
ylabel('x(t)');
title('Sinal Modulado');
xlim([0 0.01]); % Zoom no eixo x
ylim([-1.5 1.5]); % Ajuste no eixo y
