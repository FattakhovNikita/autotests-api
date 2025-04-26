from pydantic import BaseModel, Field, ConfigDict

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str | None = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение курса
    """
    user_id: str = Field(alias="userId")

class GetCoursesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения курсов
    """
    model_config = ConfigDict(populate_by_name=True)

    courses: list[CourseSchema]


class GetCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения курсов
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema


class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    preview_file_id: str = Field(alias="previewFileId")
    estimated_time: str | None = Field(alias="estimatedTime")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str | None
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления курса
    """
    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema

