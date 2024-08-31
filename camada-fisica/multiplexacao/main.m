% Configurações do sinal
Fs = 1e4;          % Frequência de amostragem (10 kHz)
T = 1;             % Duração do sinal (1 s)
t = 0:1/Fs:T-1/Fs; % Vetor de tempo

% Sinais individuais
f1 = 1;            % Frequência do sinal 1 (1 Hz)
f2 = 3;            % Frequência do sinal 2 (3 Hz)
f3 = 5;            % Frequência do sinal 3 (5 Hz)

sinal1 = sin(2*pi*f1*t); % Sinal 1
sinal2 = sin(2*pi*f2*t); % Sinal 2
sinal3 = sin(2*pi*f3*t); % Sinal 3

% Multiplexação TDM
% Definindo o intervalo de tempo para cada sinal
intervalo = 0.1; % 100 ms para cada sinal
amostras_intervalo = round(intervalo * Fs); % Número de amostras por intervalo

% Inicializando o sinal multiplexado
sinal_multiplexado = zeros(size(t));

% Inserindo cada sinal em sua faixa de tempo
for k = 0:2
    start_idx = k*amostras_intervalo + 1;
    end_idx = min((k+1)*amostras_intervalo, length(t));
    if k == 0
        sinal_multiplexado(start_idx:end_idx) = sinal1(1:(end_idx-start_idx+1));
    elseif k == 1
        sinal_multiplexado(start_idx:end_idx) = sinal2(1:(end_idx-start_idx+1));
    else
        sinal_multiplexado(start_idx:end_idx) = sinal3(1:(end_idx-start_idx+1));
    end
end

% Demultiplexação TDM
% Inicializando os sinais demultiplexados
sinal_demux1 = zeros(size(t));
sinal_demux2 = zeros(size(t));
sinal_demux3 = zeros(size(t));

% Extraindo cada sinal do sinal multiplexado
for k = 0:2
    start_idx = k*amostras_intervalo + 1;
    end_idx = min((k+1)*amostras_intervalo, length(t));
    if k == 0
        sinal_demux1(start_idx:end_idx) = sinal_multiplexado(start_idx:end_idx);
    elseif k == 1
        sinal_demux2(start_idx:end_idx) = sinal_multiplexado(start_idx:end_idx);
    else
        sinal_demux3(start_idx:end_idx) = sinal_multiplexado(start_idx:end_idx);
    end
end

% Plotagem dos sinais
figure;

subplot(4,1,1);
plot(t, sinal1);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal 1');

subplot(4,1,2);
plot(t, sinal2);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal 2');

subplot(4,1,3);
plot(t, sinal3);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal 3');

subplot(4,1,4);
plot(t, sinal_multiplexado);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Multiplexado');

% Plotagem dos sinais demultiplexados
figure;

subplot(3,1,1);
plot(t, sinal_demux1);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Demultiplexado 1');

subplot(3,1,2);
plot(t, sinal_demux2);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Demultiplexado 2');

subplot(3,1,3);
plot(t, sinal_demux3);
xlabel('Tempo (s)');
ylabel('Amplitude');
title('Sinal Demultiplexado 3');
