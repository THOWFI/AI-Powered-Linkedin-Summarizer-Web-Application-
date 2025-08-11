from typing import List, Dict, Any

from pydantic.v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class Person(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    Educational_Background: List[str] = Field(description="Educational background of the person")
    Skills: List[str] = Field(description="Skills of the person")
    Work_Experience: List[str] = Field(description="Work experience of the person")
    Career_Progression: str = Field(description="Career progression (e.g., job transitions, promotions, or role changes)")
    Key_Achievements: List[str] = Field(description="Key achievements (e.g., notable projects, awards, or impacts mentioned)")
    Cultural_Fit_Indicators: str = Field(description="Cultural fit indicators (e.g., traits or values inferred from the profile that might align with team dynamics")
    Linkedin_Summarizers: List[str] = Field(description="Create linkedin summarizer to open a conversation with person")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "Educational_Background":self.Educational_Background,
            "Skills":self.Skills,
            "Work_Experience":self.Work_Experience,
            "Career_Progression":self.Career_Progression,
            "Key_Achievements":self.Key_Achievements,
            "Cultural_Fit_Indicators":self.Cultural_Fit_Indicators,
            "Linkedin_Summarizer":self.Linkedin_Summarizer
        }


class Linkedin_Summarizer(BaseModel):
    Linkedin_Summarizers: List[str] = Field(description="Linkedin Summarizer list")

    def to_dict(self) -> Dict[str, Any]:
        return {"Linkedin_Summarizers": self.Linkedin_Summarizers}


class TopicOfInterest(BaseModel):
    topics_of_interest: List[str] = Field(
        description="topic that might interest the person"
    )

    def to_dict(self) -> Dict[str, Any]:
        return {"topics_of_interest": self.topics_of_interest}


summary_parser = PydanticOutputParser(pydantic_object=Person)
linkedin_summarizer_parser = PydanticOutputParser(pydantic_object=Linkedin_Summarizer)
topics_of_interest_parser = PydanticOutputParser(pydantic_object=TopicOfInterest)
