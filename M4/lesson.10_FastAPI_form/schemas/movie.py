from datetime import date
from pydantic import BaseModel, Field, field_validator  #Старый способ -  @validator
from typing import Optional


class MovieBase(BaseModel):

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Movie Title",
        examples=['The Matrix', 'Game', 'I am Robot']
    )
    year: int = Field(
        ...,
        # ge=1850,
        # le=date.today().year,
        description="Movie Year",
        examples=[1999, 2000, 2015],
    )
    description: str | None = Field(
        None,
        description="Movie Description",
        examples=['Фантастический фильм про виртуальную реальность'],
    )

    genre_id: int | None = Field(
        None,
        description="Genre id",
        examples=[1, 2, 3],
    )

    # @validator - устаревшее

    @field_validator('title')
    @classmethod # рекомендуется указывать
    def normalize_title(cls, value: str) -> str:
        clean_value = value.strip()

        if not clean_value:
            raise ValueError('Заголовок не может состоять из одних пробелов.')

        return clean_value


    @field_validator('year')
    @classmethod # рекомендуется указывать
    def check_year(cls, value: str) -> str:
        current_year = date.today().year

        if value > current_year:
            raise ValueError('Год не должен быть больше текущего года')

        if value < 1850:
            raise ValueError('Год не должен быть меньше 1850 года')

        return value


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Movie Title",
        examples=['The Matrix', 'Game', 'I am Robot']
    )
    year: Optional[int] = Field(
        None,
        ge=1800,
        le=date.today().year,
        description="Movie Year",
        examples=[1999, 2000, 2015],
    )
    description:  Optional[str] = Field(
        None,
        description="Movie Description",
        examples=['Фантастический фильм про виртуальную реальность'],
    )

    genre_id: Optional[int] = Field(
        None,
        description="Genre id",
        examples=[1, 2, 3],
    )



class MovieInDBBase(MovieBase):
    id: int = Field(
        ...,
        description="Movie ID",
        examples=[1, 2, 3, 4, 5]
    )
    # class Config:
    #     orm_mode = True


class MoviePublic(MovieInDBBase):
    pass



movie_list = [
    MovieInDBBase(
        id=1,
        title="Mатрица",
        year=1999,
        description="Movie Description 1",
    ),
    MovieInDBBase(
        id=2,
        title="Звездные войны",
        year=1981,
        description="Movie Description 2",
    ),
    MovieInDBBase(
        id=3,
        title="Игра",
        year=1999,
        description="Movie Description 3",
    ),
    MovieInDBBase(
        id=4,
        title="Игра престолов",
        year=2005,
        description="Movie Description 4",
    ),
    MovieInDBBase(
        id=5,
        title="Терминатор",
        year=1987,
        description="Movie Description 5",
    ),
]