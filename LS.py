from langchain_google_genai import ChatGoogleGenerativeAI  
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain 
from dotenv import load_dotenv
import os
import google.generativeai as genai
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import summary_parser, Person

load_dotenv(override=True)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def linkedin_summarizer(name: str) -> tuple[Person, str]: 
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    summary_template = ChatPromptTemplate.from_messages([
        ("system", "You are an AI assistant that provides structured summaries."),
        ("human", """Given the following LinkedIn profile information: {information}

Please provide a structured summary in JSON format with the following structure:
```json
{{
  "summary": "A brief summary of the person's profile",
  "facts": ["Interesting fact 1", "Interesting fact 2"],
  "Educational_Background": ["Degree, Institution, Year"],
  "Skills": ["Skill 1", "Skill 2"],
  "Work_Experience": ["Role, Company, Duration"],
  "Career_Progression": "Description of job transitions or promotions",
  "Key_Achievements": ["Achievement 1", "Achievement 2"],
  "Cultural_Fit_Indicators": "Traits or values that align with team dynamics",
  "Linkedin_Summarizers": ["Conversation starter 1"]
}}
```""")
    ])

    summary_prompt_template = ChatPromptTemplate(
        input_variables=["information"],
        messages=summary_template.messages
    )

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
    chain = summary_prompt_template | llm
    result = chain.invoke({"information": linkedin_data})
    parsed_result = summary_parser.parse(result.content)
    return parsed_result, linkedin_data.get("profile_pic_url")

if __name__ == "__main__":
    print("hello langchain")
    linkedin_summarizer(name="Harinesh MA A")