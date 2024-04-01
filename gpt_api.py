import openai
from dotenv import load_dotenv, dotenv_values
load_dotenv()
import os

openai.api_key = os.getenv("MY_KEY")  


def comp(PROMPT, MaxToken=50, outputs=3): 
	response = openai.Completion.create(  
		model="gpt-3.5-turbo-instruct", 
		prompt=PROMPT, 
		max_tokens=MaxToken, 
		n=outputs 
	) 
	output = list() 
	for k in response['choices']: 
		output.append(k['text'].strip()) 
	return output


if __name__=="__main__":
    val = comp("what is the purpose of life ?", MaxToken=3000, outputs=3)
    print(val)