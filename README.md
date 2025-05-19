# EazyYT - Simple YouTube Downloader  
![Screenshot](https://i.imgur.com/DP99oZY.png)

- **English version:** [English](#english)
- **Versão pt-BR:** [pt-br](#pt-br)

---

## English

EazyYT is a simple graphical application designed to easily download YouTube videos or extract audio from them. Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a modern GUI and [yt_dlp](https://github.com/yt-dlp/yt-dlp) for downloading, EazyYT lets you choose between downloading videos in MP4 format or extracting audio in MP3. It also supports playlist detection, offering the option to download the full playlist or just a single video.

### Features
- **Modern GUI:** Interface built with CustomTkinter featuring a sleek dark theme.
- **Format Selection:** Option to download videos (MP4) or extract audio (MP3).
- **Playlist Support:** Automatically detects if the provided YouTube link includes a playlist and asks whether to download the entire list.
- **Error Handling:** Displays a pop-up message if an invalid link is entered.

### Requirements
- Python 3.x  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)  
- FFmpeg (needed for MP3 extraction)

### Installation
1. Clone the repository from GitHub.
2. Install the required packages listed in requirements section

### Usage
- **Run the Application:** Simply run the script with Python, or if your os is windows, you run the exe.
- **How It Works:**  
  1. Enter a valid YouTube link (starting with `https://www.youtube.com/watch?v=`) in the input field.  
  2. Choose the desired format (MP4 for video or MP3 for audio) using the option menu.  
  3. Click the **Download!** button.  
  4. If the link belongs to a playlist, a pop-up will prompt you to choose between downloading the full playlist or just the individual video.  
  5. After the download completes, a confirmation pop-up will appear.  
  6. Check the appropriate folder (either `mp4` or `mp3`) in the main directory for your downloaded file.

---

## pt-BR

EazyYT é uma aplicação gráfica simples criada para facilitar o download de vídeos do YouTube ou a extração do áudio desses vídeos. Desenvolvido com [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) para uma interface moderna e [yt_dlp](https://github.com/yt-dlp/yt-dlp) para o download, o EazyYT permite escolher entre baixar vídeos em formato MP4 ou extrair áudio em MP3. Ele também possui suporte para playlists, perguntando se deseja baixar a playlist completa ou apenas um vídeo individual.

### Funcionalidades
- **Interface Moderna:** Interface gráfica construída com CustomTkinter com aparência escura.
- **Seleção de Formato:** Opção para baixar vídeos (MP4) ou extrair áudio (MP3).
- **Suporte a Playlists:** Detecta se o link do YouTube faz parte de uma playlist e pergunta se o usuário deseja baixar a lista completa.
- **Tratamento de Erros:** Exibe uma janela pop-up caso um link inválido seja inserido.

### Requisitos
- Python 3.x  
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)  
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)  
- FFmpeg (necessário para extração de MP3)

### Instalação
1. Clone o repositório do GitHub.
2. Instale os pacotes necessários conforme indicado na parte de requisitos

### Uso
- **Execute a Aplicação:** Rode o script utilizando o Python, ou caso seu sistema seja windows, rode o exe.
- **Como Funciona:**  
  1. Insira um link válido do YouTube (começando com `https://www.youtube.com/watch?v=`) no campo de entrada.  
  2. Selecione o formato desejado (MP4 para vídeo ou MP3 para áudio) no menu de opções.  
  3. Clique no botão **Download!**.  
  4. Se o link pertencer a uma playlist, uma janela pop-up perguntará se você deseja baixar a playlist completa ou apenas o vídeo individual.  
  5. Após o download ser concluído, uma janela de confirmação será exibida.  
  6. Verifique as pastas correspondentes (`mp4` ou `mp3`) no diretório principal para encontrar o arquivo baixado.


:)
