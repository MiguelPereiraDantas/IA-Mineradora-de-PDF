# pdf_model.py
import re
from pdfminer.high_level import extract_text
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
nltk.download('punkt')

class PDFProcessor:
    def filtrar_palavra(self, pdf_path, palavra):
        texto = self.extrair_texto(pdf_path)
        palavras = self.tokenizar_texto(texto)
        palavras_filtradas = self.filtrar_palavras(palavras, palavra)
        return palavras_filtradas

    def extrair_texto(self, pdf_path):
        return extract_text(pdf_path)

    def tokenizar_texto(self, texto):
        return word_tokenize(texto)

    def filtrar_palavras(self, palavras, palavra):
        stop_words = set(stopwords.words('portuguese'))
        palavras = [word for word in palavras if word.lower() not in stop_words]
        palavras_filtradas = [word for word in palavras if re.match(fr'\b{re.escape(palavra)}\b', word, flags=re.IGNORECASE)]
        return palavras_filtradas
