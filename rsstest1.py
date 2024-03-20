from langchain_community.document_loaders import RSSFeedLoader
from langchain import OpenAI
llm = OpenAI(temperature=0., model="gpt-3.5-turbo-instruct")

#import nltk
#nltk.download('punkt')

#from langchain.callbacks import get_openai_callback

urls = ["http://www.newsblur.com/reader/starred_rss/605591/89d85fb786d7/tech"]


loader = RSSFeedLoader(urls=urls, nlp=True)

data = loader.load()
numberofentries = (len(data))
print(numberofentries)
print("""



""")

print(data[0].page_content)

#write a function to now evaluate rss entries for their "interestingfulness"


print(data[0].metadata["keywords"])
