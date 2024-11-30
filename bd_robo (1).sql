-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 30/11/2024 às 20:14
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bd_robo`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `dispositivo`
--

CREATE TABLE `dispositivo` (
  `id_dispositivo` int(11) NOT NULL,
  `cod_dispositivo` varchar(100) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `tipo_dispositivo` varchar(50) NOT NULL,
  `data_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `posicao`
--

CREATE TABLE `posicao` (
  `id_posicao` int(11) NOT NULL,
  `id_rotina` int(11) DEFAULT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `eixoA` int(11) NOT NULL,
  `eixoB` int(11) NOT NULL,
  `eixoC` int(11) NOT NULL,
  `eixoD` int(11) NOT NULL,
  `eixoE` int(11) NOT NULL,
  `eixoF` int(11) NOT NULL,
  `data_registro` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `posicao`
--

INSERT INTO `posicao` (`id_posicao`, `id_rotina`, `nome`, `descricao`, `eixoA`, `eixoB`, `eixoC`, `eixoD`, `eixoE`, `eixoF`, `data_registro`) VALUES
(12, NULL, 'Movimento1', NULL, 2318, 2692, 0, 0, 0, 0, '2024-11-23 02:48:24'),
(13, NULL, 'Movimento2', NULL, 513, 2692, 0, 0, 0, 0, '2024-11-23 02:48:35'),
(14, NULL, 'Movimento3', NULL, 513, 1095, 0, 0, 0, 0, '2024-11-23 02:48:43'),
(15, NULL, 'Movimento4', NULL, 3636, 367, 0, 0, 0, 0, '2024-11-23 02:57:38'),
(16, NULL, 'Posição 5', NULL, 2491, 2761, 0, 0, 0, 0, '2024-11-23 04:19:51'),
(17, NULL, 'Posição5', NULL, 2491, 2761, 0, 0, 0, 0, '2024-11-23 04:19:58'),
(18, NULL, 'Movimento5', NULL, 3324, 2692, 0, 0, 0, 0, '2024-11-23 04:32:31'),
(19, NULL, 'Movimento6', NULL, 929, 922, 0, 0, 0, 0, '2024-11-23 11:20:52');

-- --------------------------------------------------------

--
-- Estrutura para tabela `rotina`
--

CREATE TABLE `rotina` (
  `id_rotina` int(11) NOT NULL,
  `cod_rotina` int(11) NOT NULL,
  `id_dispositivo` int(11) DEFAULT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `tamanho_rotina` int(11) DEFAULT NULL,
  `data_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `super_usuario`
--

CREATE TABLE `super_usuario` (
  `id_super` int(11) NOT NULL,
  `cod_super` varchar(100) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(50) NOT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  `data_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `cod_usuario` varchar(100) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `login` varchar(50) NOT NULL,
  `senha` varchar(50) NOT NULL,
  `data_registro` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `cod_usuario`, `nome`, `descricao`, `login`, `senha`, `data_registro`) VALUES
(1, '2asd232', 'Teste', NULL, 'teste', '1234', '2024-09-29 12:05:54');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `dispositivo`
--
ALTER TABLE `dispositivo`
  ADD PRIMARY KEY (`id_dispositivo`),
  ADD UNIQUE KEY `cod_dispositivo` (`cod_dispositivo`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Índices de tabela `posicao`
--
ALTER TABLE `posicao`
  ADD PRIMARY KEY (`id_posicao`),
  ADD KEY `posicao_rotina` (`id_rotina`);

--
-- Índices de tabela `rotina`
--
ALTER TABLE `rotina`
  ADD PRIMARY KEY (`id_rotina`),
  ADD UNIQUE KEY `cod_rotina` (`cod_rotina`),
  ADD KEY `id_dispositivo` (`id_dispositivo`);

--
-- Índices de tabela `super_usuario`
--
ALTER TABLE `super_usuario`
  ADD PRIMARY KEY (`id_super`),
  ADD UNIQUE KEY `cod_usuario` (`cod_super`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `cod_usuario` (`cod_usuario`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `dispositivo`
--
ALTER TABLE `dispositivo`
  MODIFY `id_dispositivo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `posicao`
--
ALTER TABLE `posicao`
  MODIFY `id_posicao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `rotina`
--
ALTER TABLE `rotina`
  MODIFY `id_rotina` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `super_usuario`
--
ALTER TABLE `super_usuario`
  MODIFY `id_super` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `dispositivo`
--
ALTER TABLE `dispositivo`
  ADD CONSTRAINT `dispositivo_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`);

--
-- Restrições para tabelas `posicao`
--
ALTER TABLE `posicao`
  ADD CONSTRAINT `posicao_rotina` FOREIGN KEY (`id_rotina`) REFERENCES `rotina` (`id_rotina`) ON DELETE SET NULL;

--
-- Restrições para tabelas `rotina`
--
ALTER TABLE `rotina`
  ADD CONSTRAINT `rotina_ibfk_1` FOREIGN KEY (`id_dispositivo`) REFERENCES `dispositivo` (`id_dispositivo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
