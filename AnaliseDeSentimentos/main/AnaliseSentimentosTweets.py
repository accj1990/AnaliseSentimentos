from textblob import TextBlob
from googletrans import Translator
import csv
import sys
class AnaliseSentimentosTweets (object):
	def __init__(self, path):
		self.path = path
		self.translator = Translator()
	def lerArquivo(self):
		with open(self.path, encoding='utf-8') as datafile:
			reader = csv.reader(datafile, delimiter=';', quoting=csv.QUOTE_NONE)
			non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
			for linha in reader:
				textoConvertido = str(linha[7]).translate(non_bmp_map)
				print(textoConvertido)
				texto = self.traduzirTexto(textoConvertido)
				self.analisarSentimento(texto)
				
	def traduzirTexto(self, texto):
		return self.translator.translate(texto).text
	
	def analisarSentimento(self, text):
		testimonial = TextBlob(text)
		testimonial.sentiment
		print(testimonial.sentiment.polarity)
