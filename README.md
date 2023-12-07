# Filtrar Palavra em PDF - Aplicação Python com Suporte a Múltiplos Idiomas

## Descrição

Este é um programa Python simples que permite filtrar ocorrências de uma palavra específica em um arquivo PDF. A aplicação utiliza a biblioteca Tkinter para a interface gráfica, PDFMiner para a extração de texto de arquivos PDF, e NLTK para processamento de linguagem natural.

O código foi organizado seguindo a arquitetura MVC (Model-View-Controller), facilitando a manutenção e a expansão da aplicação. Além disso, foram implementados recursos adicionais para aprimorar a experiência do usuário, como suporte a múltiplos idiomas, barra de menus, ícone na janela e barra de progresso.

## Funcionalidades

- **Filtragem de Palavra em PDF:** O usuário pode inserir uma palavra específica e selecionar um arquivo PDF para buscar ocorrências dessa palavra no texto.

- **Barra de Menus:** Uma barra de menus fornece opções adicionais, incluindo a opção de sair do aplicativo.

- **Suporte a Múltiplos Idiomas:** O aplicativo é internacionalizável, permitindo a tradução das strings de texto para diferentes idiomas. Atualmente, há suporte para inglês e português.

- **Barra de Progresso:** Uma barra de progresso indica a atividade durante o processamento do arquivo PDF.

## Pré-requisitos

Certifique-se de ter o Python 3.x instalado no seu sistema. Além disso, instale as dependências necessárias usando o seguinte comando:

```bash
pip install pdfminer.six nltk
```
## Como Executar

### Clone este repositório:

```bash
git clone https://github.com/MiguelPereiraDantas/IA-Mineradora-de-PDF.git
cd IA-Mineradora-de-PDF
```
### Execute o programa:

```bash
python main.py
```
Selecione um arquivo PDF, insira a palavra a ser filtrada e clique no botão "Selecionar Arquivo PDF".

## Configuração de Idioma

Antes de executar o programa, configure o idioma desejado usando a variável de ambiente `LANG`. Por exemplo, para executar em português:

```bash
export LANG=pt_BR.UTF-8
python main.py
```
ou configure diretamente no código antes de chamar mainloop():

```python
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
```

Certifique-se de substituir 'pt_BR.UTF-8' pelo código do idioma desejado.

```perl
Isso fornece instruções claras sobre como configurar o idioma antes de executar o programa, seja usando a variável de ambiente `LANG` ou configurando diretamente no código Python.
```
## Autor

[Miguel Pereira Dantas de Oliveira](https://github.com/MiguelPereiraDantas)
