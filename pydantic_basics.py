from pydantic import BaseModel, Field, ConfigDict, computed_field, EmailStr, HttpUrl, ValidationError
from pydantic.alias_generators import to_camel
import uuid

"""
{
  "courses": [
    {
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
  ]
}
"""


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class FileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "course-id"
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias="estimatedTime", default="AI")
    created_by_user: UserSchema = Field(alias="createdByUser")


course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    previewFile=FileSchema(
        id="file-id",
        url="http://localhost:8000",
        filename="image.png",
        directory="courses"
    ),
    description="Playwright",
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="user-id",
        email="bb@mail.com",
        lastName="test",
        firstName="test",
        middleName="test"
    )
)
print('Course default model', course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "file-id",
        "url": "http://localhost:8000",
        "filename": "inage.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "user-id",
        "email": "bb@mail.com",
        "lastName": "Goota",
        "firstName": "Anna",
        "middleName": "test"
    }
}

course_dict_model = CourseSchema(**course_dict)

print('Course dict model', course_dict_model)

course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile":{
        "id":"file-id",
        "url":"http://localhost:8000",
        "filename":"inage.png",
        "directory":"courses"
    },
    "estimatedTime": "1 week",
    "createdByUser":{
        "id": "user-id",
        "email": "bb@mail.com",
        "lastName": "test",
        "firstName": "test",
        "middleName": "test"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course json model', course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))
try:
    user = UserSchema(
        id="user-id",
        email="lala@mail.com",
        lastName="Goota",
        firstName="Anna",
        middleName="test"
    )
    print(user.get_username(), user.username)
except ValidationError as error:
    print(error)
    print(error.errors())
