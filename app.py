import warnings
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.data_anonymizer import PresidioAnonymizer
from prompt_template import data_masking_prompt

warnings.filterwarnings('ignore')
_ = load_dotenv()

llm = ChatOpenAI(model="gpt-4o-2024-05-13", temperature=0)

loader = TextLoader("claim.txt")

claim_text = loader.load()[0].page_content

anonymizer = PresidioAnonymizer()

template = data_masking_prompt

prompt = PromptTemplate.from_template(template)

chain = {"INSURANCE_CLAIM_DOCUMENT": anonymizer.anonymize} | prompt | llm
response = chain.invoke(claim_text)
print(response.content)


