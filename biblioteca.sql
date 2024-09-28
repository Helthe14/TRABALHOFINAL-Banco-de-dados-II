-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28/09/2024 às 20:35
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `biblioteca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_aluno`
--

CREATE TABLE `tb_aluno` (
  `id` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `matricula` varchar(20) NOT NULL,
  `curso` varchar(100) NOT NULL,
  `nivel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_aluno`
--

INSERT INTO `tb_aluno` (`id`, `nome`, `matricula`, `curso`, `nivel`) VALUES
(1, 'Helther Lima', '123123', 'Ciências da Computação', 'Graduação'),
(2, 'Livia Fox', '512565', 'Engenharia de Software', 'Pós-graduação'),
(3, 'Lucas Pitonn', '558832', 'Matemática', 'Graduação'),
(14, 'Lohan Fox', '558844', 'Química', 'Doutorado'),
(21, 'Luci Luau', '995599', 'Letras', 'Mestrado'),
(25, 'Lucas Lina', '889988', 'Letras', 'Mestrado'),
(27, 'Lucas Jhon', '333222', 'Letras', 'Mestrado');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_emprestimo`
--

CREATE TABLE `tb_emprestimo` (
  `id` int(11) NOT NULL,
  `id_aluno` int(11) DEFAULT NULL,
  `id_livro` int(11) DEFAULT NULL,
  `data` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_emprestimo`
--

INSERT INTO `tb_emprestimo` (`id`, `id_aluno`, `id_livro`, `data`) VALUES
(20, 1, 3, '2024-09-27 20:28:37'),
(23, 1, 1, '2024-09-27 20:43:37');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_livro`
--

CREATE TABLE `tb_livro` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `ano` year(4) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `id_status` int(11) NOT NULL DEFAULT 1,
  `imagem` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_livro`
--

INSERT INTO `tb_livro` (`id`, `nome`, `ano`, `autor`, `id_status`, `imagem`) VALUES
(1, 'Dom Quixote de La Mancha', '2012', 'Miguel de Cervantes', 2, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/Dom-Quixote-de-La-Mancha-Miguel-de-Cervantes._240x240.jpg?v=1626441834'),
(2, 'Metamorfose', '2000', 'Franz Kafka', 1, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/Metamorfose-Franz-Kafka_240x240.jpg?v=1626441860'),
(3, 'Ensaio Sobre a Cegueira', '2006', 'José Saramago', 2, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/Ensaio-Sobre-a-Cegueira-Jose-Saramago._240x240.jpg?v=1626441891'),
(4, 'Crime e Castigo', '2005', 'Fiódor Dostoiévsky M', 1, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/Crime-e-Castigo-Fiodor-Dostoievsky._240x240.jpg?v=1626441912'),
(5, 'O Sol é Para Todos', '2005', 'Harper Lee', 1, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/O-Sol-e-Para-Todos-Harper-Lee._240x240.jpg?v=1626441978'),
(6, 'Os Miseráveis', '1999', 'Victor Hugo', 1, 'https://cdn.shopify.com/s/files/1/0296/8358/1021/files/Os-Miseraveis-Victor-Hugo._240x240.jpg?v=1626442014'),
(8, 'Drácula', '2002', ' Stoker', 1, 'https://a-static.mlcdn.com.br/800x560/livro-dracula-dark-edition/magazineluiza/224356900/0112c064b96b92600b286b082afb1b67.jpg'),
(9, 'A arte da guerra', '2019', 'Pedro Manoel', 1, 'https://a-static.mlcdn.com.br/800x560/livro-a-arte-da-guerra/cliquebooks/570490-1/983c516760101c1ba365279a462fdd10.jpeg'),
(10, 'Teoria da Música', '2015', 'Bohumil Med', 1, 'https://m.media-amazon.com/images/I/61X1NRhxd7L._AC_UY218_.jpg'),
(11, 'Perigoso!', '2024', 'Harper Lee', 1, 'https://m.media-amazon.com/images/I/71HsNbyBPBL._SY425_.jpg'),
(12, 'O poder do hábito', '2022', ' Stoker', 1, 'https://m.media-amazon.com/images/I/815iPX0SgkL._SY425_.jpg'),
(13, 'Os segredos da mente milionária', '2022', 'José Saramago', 1, 'https://m.media-amazon.com/images/I/81WzW3xJb5L._SY425_.jpg'),
(14, 'O homem mais rico da Babilônia', '1980', 'José Saramago', 1, 'https://m.media-amazon.com/images/I/81ehX6Quw2L._SY425_.jpg'),
(15, 'Pai Rico, pai Pobre', '2024', 'Harper Lee', 1, 'https://m.media-amazon.com/images/I/81ALgAW3gHL._SY425_.jpg'),
(16, 'A Garota do Lago Charlie Donlea', '2012', 'José Saramago', 1, 'https://a-static.mlcdn.com.br/800x560/livro-a-garota-do-lago-charlie-donlea/magazineluiza/226335300/50ddcc1f2a5098685122c349a1b06453.jpg'),
(17, 'Nunca foi sorte', '2015', 'Fiódor Dostoiévsky', 1, 'https://a-static.mlcdn.com.br/800x560/livro-nunca-foi-sorte/magazineluiza/223794900/b4f33b50e8a94f4483570800d5930e8b.jpg'),
(18, 'A ciência do sucesso', '2012', 'Harper Lee', 1, 'https://a-static.mlcdn.com.br/800x560/livro-a-ciencia-do-sucesso-livro-de-bolso/magazineluiza/227661500/8f79a4b3411e2da785e13a5940189593.jpg'),
(19, 'A escada para o triunfo', '2020', 'José Saramago', 1, 'https://a-static.mlcdn.com.br/800x560/livro-a-escada-para-o-triunfo-livro-de-bolso/magazineluiza/227661600/a4bc5cf6f07f9d1c65fcdf1395665166.jpg');

-- --------------------------------------------------------

--
-- Estrutura para tabela `tb_status`
--

CREATE TABLE `tb_status` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `tb_status`
--

INSERT INTO `tb_status` (`id`, `status`) VALUES
(1, 'Disponivel'),
(2, 'Emprestado');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `tb_aluno`
--
ALTER TABLE `tb_aluno`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `tb_emprestimo`
--
ALTER TABLE `tb_emprestimo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_aluno` (`id_aluno`),
  ADD KEY `id_livro` (`id_livro`);

--
-- Índices de tabela `tb_livro`
--
ALTER TABLE `tb_livro`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_status` (`id_status`);

--
-- Índices de tabela `tb_status`
--
ALTER TABLE `tb_status`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tb_aluno`
--
ALTER TABLE `tb_aluno`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de tabela `tb_emprestimo`
--
ALTER TABLE `tb_emprestimo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de tabela `tb_livro`
--
ALTER TABLE `tb_livro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de tabela `tb_status`
--
ALTER TABLE `tb_status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `tb_emprestimo`
--
ALTER TABLE `tb_emprestimo`
  ADD CONSTRAINT `tb_emprestimo_ibfk_1` FOREIGN KEY (`id_aluno`) REFERENCES `tb_aluno` (`id`),
  ADD CONSTRAINT `tb_emprestimo_ibfk_2` FOREIGN KEY (`id_livro`) REFERENCES `tb_livro` (`id`);

--
-- Restrições para tabelas `tb_livro`
--
ALTER TABLE `tb_livro`
  ADD CONSTRAINT `tb_livro_ibfk_1` FOREIGN KEY (`id_status`) REFERENCES `tb_status` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
