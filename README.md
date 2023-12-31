# Pratica-6-Sistemas-Embarcados
## Introdução às interfaces de visão computacional, controle de acesso, versionamento e repositório de códigos
##### Prof. Pedro Oliveira
##### Gabriel Aguilar Soares de Melo N° 11915432
##### João Pedro Suzuki de Figueiredo N° 11800712

### Resumo da Atividade Prática
Nesta prática exploramos o uso de periféricos embarcados na Raspberry Pi com o uso do módulo de câmera, tag RFID, aprendizado de máquina, e controle de versão via Git/GitHub, como base para projetos de controle de acesso via tags e reconhecimento facial em banco de dados e servidores.

### Conceitos Importantes Abordados
OpenCV, PiCamera, visão computacional, Git/GitHub, RFID, banco de dados, web server, SPI, machine learning.

### Objetivos da Prática
O objetivo desta prática é desenvolver um projeto que sirva de base para controle de acesso via tags e para reconhecimento facial em sistemas embarcados. Para isto, será utilizado uma comunicação SPI com tag RFID (radio frequency identification) para controle de acesso e o módulo da câmera embarcado na Raspberry Pi. Como forma de documentação do projeto, o Git será o sistema de versionamento e o GitHub como repositório, junto do histórico de versionamento. 

Para o controle de acesso via tag, será utilizado o módulo RFID-MFRC522 , que usa a tecnologia de identificação por rádio frequência. O RFID opera com frequências altas e é capaz de gravar informações nos cartões, que possuem um CI e memória programável. A comunicação do RFID-MFRC522 com o sistema embarcado é feita via SPI (Serial Peripheral Interface), o qual é um protocolo de comunicação serial síncrona de curtas distâncias usado para a troca de dados entre dispositivos como SBCs, microcontroladores e periféricos.

### Roteiro das Atividades
##### 1 - Controle de Acesso via Tag RFID:
Estabeleça a configuração do circuito RFID-RC522 seguindo as devidas conexões. Ative a comunicação SPI na Raspberry Pi e instale a biblioteca Python relacionada ao módulo RFID. Desenvolva scripts para escrever texto no módulo RFID, identificando o ID da Tag. Em seguida, elabore um programa em Python que, ao aproximar a Tag, ative um LED verde indicando "acesso liberado" ou um LED vermelho indicando "acesso negado".

###### 2 - Parte da Câmera:
Conecte a câmera à Raspberry Pi enquanto ela estiver desligada e teste seu funcionamento usando o comando libcamera-hello. Em seguida, faça o download do algoritmo Haar Cascade e instale as bibliotecas Python OpenCV e PiCamera2. Desenvolva um script para detectar rostos e apresente seu funcionamento prático, documentando-o com fotos da montagem física e capturas de tela da Raspberry Pi.

##### 3 - Git e GitHub:
Primeiramente, estabeleça a configuração do Git na Raspberry Pi para gerenciar as versões do projeto. Em seguida, crie uma conta no GitHub e um repositório para documentar o desenvolvimento. Clone esse repositório na Raspberry Pi, adicione os programas em Python, faça commits regulares e envie as atualizações para o GitHub. Crie um arquivo README.md explicando o funcionamento básico do projeto. No terminal do repositório local, utilize o comando git log para visualizar o histórico de commits, e salve esse registro em um arquivo de texto.

### Implementação:

##### RFID-MFRC522
Para a implementação do leitor RFID, foi realizada a montagem da Figura 1 abaixo, utilizando o protoboard disponível em aula:

<div align="center">
  <img src="https://github.com/GabrielASMelo/Pratica-6-Sistemas-Embarcados/assets/153654228/4aa7eaca-6f48-466b-b387-53c7d9361632" height="500px" width="500px">
</div>

Utilizamos também a tabela de conexões apresentada abaixo, de modo que os respectivos pinouts da Rasperry foram interligados com os Módulos RFID, como mostra na Tabela 1:

<div align="center">
   <img src="https://github.com/GabrielASMelo/Pratica-6-Sistemas-Embarcados/assets/153654228/2bb23eba-a7ec-4120-83e4-10c229a64270" height="400px" width="600px">
</div>

A Figura 3 mostra nosso circuito montado em sala de aula, replicando a Figura 1:

<div align="center">
<img src="https://github.com/GabrielASMelo/Pratica-6-Sistemas-Embarcados/assets/153654228/26a19257-7b67-482d-a488-3b4722d799c2" height="500px" width="500px">
</div>

A Figura 4 abaixo mostra as conexões realizadas para a montagem do mesmo:

<div align="center">
<img src="https://github.com/GabrielASMelo/Pratica-6-Sistemas-Embarcados/assets/153654228/d6e551df-ca98-46b5-9bde-c99adf97258a" height="500px" width="500px">
</div>

A aplicação dos scripts em Python fornecidos nesse repositório nos permitiu fazer o controle de acesso via Tag RFID, fazendo inicialmente o cadastro do cartão com os nossos dois últimos digitos do N°USP (12 / 32) e sinalizando uma mensagem de "Concluído", para que, depois, implementando o script de leitura em Python,  possamos verificar se o cartão está cadastrado e qual o código cadastrado no mesmo [ (12 / 32) nesse caso]. Os comandos e mensagens do terminal estão apresentados na Figura 5 abaixo, provando o funcionamento do mesmo:

<div align="center">
<img src="https://github.com/GabrielASMelo/Pratica-6-Sistemas-Embarcados/assets/153654228/ac6b14f8-cbc2-466c-b5f2-0c3aab17d4ea" height="600px" width="600px">
</div>


##### Câmera

Para a parte que envolve o uso da câmera nessa prática, não foi possível realizar o seu devido uso. O problema era identificado na própria testagem da câmera, uma vez que ela não identificava a conexão realizada e quando utilizamos o comando "libcamera-hello", aparecia como "erro", informando que não havia nenhuma câmera conectada.

Após três tentativas falhas com diferentes câmeras e conversas com o professor, percebemos que nos restaram duas explicações possíveis para o não funconamento da câmera: 
- Desgaste da entrada do "cabo flat", seja por acúmulo de poeira ou sujeira na peça, ou o "encaixe" errado;
- Uma atualização feita na Rasperry PI no início do semestre que pode ter removido o suporte para a câmera pela entrada flat, visto que esta entrou em desuso devido à sua grande quantidade de problemas.

##### Git e GitHub
Após criar uma conta no Git Hub e um repositório com código da disciplina, começamos a realizar os devidos comandos para executar e documentar o projeto dentro dele a partir da Raspberry Pi.

Inicialmente, dentro da pasta que estamos fazendo uso, utilizamos primeiramente o comando "git init" , utilizado para criar um novo repositório. Na sequência, adicionamos os arquivos em python editados durante a prática 6 para o experimento do RFID, dando os devidos commits para salvá-los dentro do repositório. Dando continuidade, para adicionar um novo controle remoto, utilizamos o comando "git remote add origin" no terminal, com a URL do nosso repositório criada para esta prática. Depois, realizamos o comando "git push origin main" para efetuar push das alterações locais para o repositório online. O "git status" vem na sequência para conferir as alterações realizadas no repositório. Por fim, utilizamos o "git log" e "git log > historicogit.txt" para salvar o histórico de comando realizados de modo que gere um arquivo .txt incluído aqui nesta entrega.
