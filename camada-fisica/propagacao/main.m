% Configurações do sinal
Fs = 1e6;          % Frequência de amostragem (1 MHz)
T = 1e-3;          % Duração do sinal (1 ms)
t = 0:1/Fs:T-1/Fs; % Vetor de tempo

% Sinal da portadora (exemplo: senoide de 100 kHz)
fc = 100e3;        % Frequência da portadora (100 kHz)
sinal_tx = cos(2*pi*fc*t); % Sinal transmitido (portadora)

% Simulação da propagação com atenuação
atenuacao = 0.5;   % Fator de atenuação (0.5 para reduzir a amplitude do sinal)
sinal_rx = atenuacao * sinal_tx; % Sinal recebido após atenuação

% Adicionando ruído branco Gaussiano ao sinal manualmente
SNR = 20; % Relação sinal-ruído em dB
potencia_sinal = mean(sinal_rx.^2); % Potência do sinal
potencia_ruido = potencia_sinal / (10^(SNR/10)); % Potência do ruído
ruido = sqrt(potencia_ruido) * randn(size(sinal_rx)); % Gera ruído
sinal_rx_ruidoso = sinal_rx + ruido; % Adiciona ruído ao sinal

% Plotagem dos sinais
figure;

% Definindo o intervalo para o zoom
zoom_start = 0;
zoom_end = 0.0001; % Exibindo apenas os primeiros 0.1 ms

subplot(3,1,1);
plot(t, sinal_tx, 'b');
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Transmitido (Portadora)');
xlim([zoom_start zoom_end]); % Aplicando zoom no eixo x

subplot(3,1,2);
plot(t, sinal_rx, 'g');
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Recebido após Atenuação');
xlim([zoom_start zoom_end]); % Aplicando zoom no eixo x

subplot(3,1,3);
plot(t, sinal_rx_ruidoso, 'r');
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Recebido com Ruído');
xlim([zoom_start zoom_end]); % Aplicando zoom no eixo x
