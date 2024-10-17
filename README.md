# CerberusTrack – Vigilância e Controle em Cada Rota
CerberusTrack é um sistema de controle de frota voltado para otimizar a gestão de veículos e operações de transporte. Composto por um dashboard para supervisores e um aplicativo móvel para motoristas, a solução oferece funcionalidades como autenticação segura, notificações por e-mail e monitoramento contínuo das rotas. Inspirado na mitologia, o nome reflete a ideia de vigilância constante e proteção. O objetivo é garantir eficiência, segurança e transparência nas operações de transporte, facilitando a tomada de decisões estratégicas e o controle operacional.
![aplicação](https://github.com/user-attachments/assets/a090208b-669f-4986-9f62-247d36b5055b)
A aplicação ajuda a organizar e monitorar a movimentação diária de veículos e pessoas. Ela permite que quem está na estrada registre, de forma simples, onde começou e terminou cada trajeto, enquanto a pessoa responsável por supervisionar tudo pode acompanhar essas informações em tempo real, através de um painel digital.
Se algo importante acontecer durante o percurso, a aplicação também pode enviar alertas automaticamente para manter todos informados. Além disso, cada acesso ao sistema é protegido com login e senha, garantindo que apenas pessoas autorizadas tenham acesso.
Com essa solução, é possível saber sempre onde estão os veículos, como estão sendo usados e se estão funcionando como esperado, ajudando a evitar falhas e melhorar a eficiência das operações.3
________________________________________

Arquitetura do Sistema CerberusTrack
1. Backend (Servidor)
•	Responsável por:
o	Escutar requisições HTTP/HTTPS em uma porta definida (ex: 443 para HTTPS).
o	Gerenciar a comunicação com o banco de dados (MySQL, PostgreSQL, ou MongoDB).
o	Enviar notificações (e-mails ou push notifications) via API ou serviços como Firebase para mobile e desktop.
o	Implementar autenticação JWT ou OAuth2 para garantir segurança.
•	Funcionalidades:
o	API REST ou GraphQL para comunicação com app mobile e dashboard.
o	Integração com serviços de localização (Google Maps API, OpenStreetMap, etc.).
o	Registros em tempo real das viagens e status dos veículos.
o	Sistema de envio de e-mails automáticos (ex: aviso de agendamento próximo ou infrações detectadas).

2. App Mobile (Motorista)
•	Funcionalidade principal:
o	Login do motorista (autenticado via backend).
o	Avaliação automática da habilitação, permissões e agendamentos futuros.
o	QR Code para identificação do veículo e início da viagem.
o	Registro de checklist do veículo:
	Status visual (ex: pneus, nível de combustível, limpeza).
	Captura de imagens via câmera integrada.
	Registro da localização GPS em cada interação.
•	Notificações:
o	Push notifications para alertas de viagem, checklist incompleto ou atraso.
________________________________________
3. Dashboard Desktop (Supervisor de Transporte)
•	Responsável por:
o	Gerenciar a frota: cadastro e atualização de veículos e motoristas.
o	Exibir em tempo real o status e localização dos veículos.
o	Monitorar alertas de viagem e notificar sobre agendamentos pendentes.
o	Visualizar relatórios sobre viagens realizadas, infrações e status dos veículos.
•	Funcionalidades:
o	Acompanhamento por mapa interativo das viagens em andamento.
o	Criação de relatórios customizáveis (PDF/Excel) sobre viagens, consumo e incidentes.
o	Integração com a aplicação de backend para sincronização contínua de dados.
________________________________________
Fluxo de Comunicação entre Componentes:
1.	Login e Autenticação
o	O motorista faz login pelo app mobile → Backend valida e retorna token JWT.
2.	Check-in com QR Code
o	App mobile lê o QR Code do veículo → Envia dados para o backend → Validação e retorno positivo para início da viagem.
3.	Checklist e Imagens
o	O motorista preenche o checklist no app mobile → Envia status e imagens para o backend, com geolocalização registrada.
4.	Atualização de Dados no Dashboard
o	Os dados de viagem e status são automaticamente atualizados no dashboard desktop para acompanhamento em tempo real.
________________________________________
Tecnologias Sugeridas:
•	Backend: Node.js, Python (Django/Flask), ou Java (Spring Boot).
•	Banco de Dados: PostgreSQL, MySQL, ou MongoDB.
•	Mobile App: Flutter ou React Native para suporte a Android e iOS.
•	Desktop Dashboard: React.js ou Angular para frontend, com Electron para versão desktop se necessário.
•	Push Notifications: Firebase Cloud Messaging (FCM).
•	Autenticação: JWT (JSON Web Tokens).
•	Hospedagem: AWS, Azure, ou DigitalOcean para alta disponibilidade.

