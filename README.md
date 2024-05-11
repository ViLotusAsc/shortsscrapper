
# Scrapper de Links de YouTube Shorts

## Visão Geral
Este projeto visa automatizar a coleta de links de shorts de um canal específico do YouTube. Ele é ideal para quem deseja analisar o conteúdo de um canal, criar compilações de vídeos ou simplesmente acompanhar os últimos uploads.

## Funcionalidades
1. Extrai links de shorts de um canal específico do YouTube.
2. Permite filtrar por data de publicação.
3. Suporta canais com milhares de shorts.
4. Exporta os links em formato CSV para fácil análise.

### Requisitos
 - Python 3.x
 - Biblioteca requests
 - Biblioteca beautifulsoup4

### Instruções de Uso
1. **Clone o Repositório**:

```git clone https://github.com/seu-usuario/scrapper-youtube-shorts.git ``` 

2. **Acesse o Diretório do Projeto**:

```cd scrapper-youtube-shorts```

3. **Edite o Arquivo config.py**:

Insira o link do canal do YouTube que você deseja raspar no campo CHANNEL_URL.
Altere o nome do arquivo de saída no campo OUTPUT_FILE.

4. **Execute o Script**:

```python main.py```

5. **Analise os Resultados**:

O arquivo txt database.txt conterá os links de todos os shorts encontrados dentro do intervalo de datas especificado. Você pode usar este arquivo para análise posterior, compilações de vídeos ou qualquer outra finalidade.

#### **Dicas**
Para canais com muitos shorts, a execução do script pode levar um tempo considerável.
Você pode ajustar o intervalo de datas para focar em um período específico.
O script pode ser facilmente modificado para atender às suas necessidades específicas.

**Contribuições**
Sinta-se à vontade para contribuir com este projeto! Envie suas sugestões, correções de bugs ou novas funcionalidades através de pull requests.

### **Observações**
Este script é apenas para fins educacionais e de pesquisa.
O uso deste script para fins comerciais ou maliciosos é estritamente proibido.
O YouTube pode bloquear o seu acesso à plataforma se detectar atividades suspeitas. Use o script com moderação e responsabilidade.

**Exemplos de Uso**
- Analisar o Conteúdo de um Canal: Utilize o script para coletar os links de todos os shorts publicados em um canal durante um determinado período. Em seguida, você pode analisar os títulos, descrições e tags dos vídeos para identificar tendências e padrões.
- Criar Compilações de Vídeos: Reúna os links de shorts de um tema específico ou período de tempo e utilize-os para criar compilações de vídeos que você pode compartilhar em suas redes sociais ou plataforma de vídeo favorita.
- Acompanhar Novos Uploads: Configure o script para ser executado periodicamente e receba notificações sobre novos uploads de shorts no canal desejado.

## **Licença**
*Este projeto está licenciado sob a licença MIT.*

### Suporte
Caso tenha dúvidas ou problemas com o script, sinta-se à vontade para abrir um issue no GitHub.


### Feito por Arthur M. V
