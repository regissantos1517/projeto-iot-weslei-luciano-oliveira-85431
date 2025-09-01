-- create_views.sql

-- 1. VIEW: Média de temperatura por dispositivo
-- Esta view calcula a temperatura média para cada dispositivo,
-- permitindo identificar quais dispositivos estão operando em temperaturas mais altas ou baixas.
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT
    device_id,
    AVG(temperature) AS avg_temp
FROM
    temperature_readings
GROUP BY
    device_id
ORDER BY
    avg_temp DESC;

-- 2. VIEW: Contagem de leituras por hora do dia
-- Esta view conta o número de leituras de temperatura por hora,
-- o que pode ajudar a identificar padrões de uso ou pico de atividade dos dispositivos
-- ao longo de um dia.
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT
    EXTRACT(HOUR FROM timestamp) AS hora,
    COUNT(*) AS contagem
FROM
    temperature_readings
GROUP BY
    hora
ORDER BY
    hora ASC;

-- 3. VIEW: Temperaturas máximas e mínimas por dia
-- Esta view retorna as temperaturas máxima e mínima registradas
-- em cada dia, sendo útil para analisar a variação diária de temperatura.
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT
    DATE(timestamp) AS data,
    MAX(temperature) AS temp_max,
    MIN(temperature) AS temp_min
FROM
    temperature_readings
GROUP BY
    data
ORDER BY
    data ASC;