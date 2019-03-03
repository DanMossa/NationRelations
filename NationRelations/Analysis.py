from google.cloud import language
from google.cloud.language import enums

class Analysis:
	#PRIVATE
	#RETURNS: JSON object containing overall sentiment and an array of sentences
	#with individual sentences
	def __analyze(self, textToAnalyze):
		#put textToAnalyze into a JSON object
		document = {'type': self.documentType_, 'content': textToAnalyze}
		#analyze_sentiment returns the JSON object with sentiment scores in them
		analysisResponse = self.client.analyze_sentiment(document)
		return analysisResponse

	#RETURNS: the overall Score of textToAnalyze
	def getSentimentScore(self, textToAnalyze):
		analysisResponse = self.analyze(textToAnalyze)
		documentSentiment =  analysisResponse.document_sentiment
		return documentSentiment.score

	#RETURNS: the overall Magnitude of textToAnalyze
	def getSentimentMagnitude(self, textToAnalyze):
		analysisResponse = self.analyze(textToAnalyze)
		documentSentiment = analysisResponse.document_sentiment
		return documentSentiment.magntiude


	#RETURNS: a tuple with format (SCORE, MAGNITUDE) of the overall textToAnalyze
	def getSentiment(self, textToAnalyze):
		analysisResponse = self.analyze(textToAnalyze)
		documentSentiment = analysisResponse.document_sentiment
		score = documentSentiment.score
		magnitude = documentSentiment.magnitude
		return (score, magnitude)

	if __name__ == '__main__':
		self.client = language.LanguageServiceCliet()
		self.documentType_ = enums.Document.Type.PLAIN_TEXT
