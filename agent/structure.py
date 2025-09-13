from pydantic import BaseModel, Field

class File(BaseModel):
    path: str = Field(description="The path to the file to be created or modified")
    purpose: str = Field(description="The purpose of the file")

class plan(BaseModel):
    name: str = Field(description = "Name of the project")
    description: str = Field(description= "A oneline description of the app to be built")
    tech: str = Field(description= "The tech stack that is to be use for the app eg: Python, Js, etc")
    features: list[str] = Field(description="A list of features that the app should have")
    files: list[File] = Field(description="A list of files to be created")