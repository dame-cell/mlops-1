from datasets import load_dataset


def ingesting():
  dataset = load_dataset("OdiaGenAI/sentiment_analysis_hindi")
  data  = dataset['train'].train_test_split(test_size=0.1)
  return data 



with open("output.txt"  , 'r' ,encoding='utf-8' )  as f:
  files = f.read()
  
