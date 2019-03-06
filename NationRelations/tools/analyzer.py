from google.cloud import language
from google.cloud.language import enums
import logging

class Analyzer:
	#PRIVATE
	#RETURNS: JSON object containing overall sentiment and an array of sentences
	#with individual sentences
	def __analyze(self, textToAnalyze):
		#put textToAnalyze in Document format
		document = {'type': self.documentType_, 'content': textToAnalyze}
		#analyze_sentiment returns 'document' with sentiment scores in them
		analysisResponse = self.language_client.analyze_sentiment(document)
		return analysisResponse

	#RETURNS: the overall Score of textToAnalyze
	def getSentimentScore(self, textToAnalyze):
		analysisResponse = self.__analyze(textToAnalyze)
		documentSentiment =  analysisResponse.document_sentiment
		return documentSentiment.score

	#RETURNS: the overall Magnitude of textToAnalyze
	def getSentimentMagnitude(self, textToAnalyze):
		analysisResponse = self.__analyze(textToAnalyze)
		documentSentiment = analysisResponse.document_sentiment
		return documentSentiment.magntiude


	#RETURNS: a tuple with format (SCORE, MAG`NITUDE) of the overall textToAnalyze
	def getSentiment(self, textToAnalyze):
		analysisResponse = self.__analyze(textToAnalyze)
		documentSentiment = analysisResponse.document_sentiment
		score = documentSentiment.score
		magnitude = documentSentiment.magnitude
		return (score, magnitude)

	def __init__(self):
		self.language_client = language.LanguageServiceClient.from_service_account_json("lang_key.json")
		self.documentType_ = enums.Document.Type.PLAIN_TEXT
		
