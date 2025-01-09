from ninja import Schema
from typing import Optional
from datetime import datetime, date
# from pydantic import BaseModel

from django.contrib.auth.models import User

class UserOut(Schema):
    id: int
    email: str
    first_name: str
    last_name: str


class CourseSchemaOut(Schema):
    id: int
    name: str
    description: str
    price: int
    image : Optional[str]
    teacher: UserOut
    created_at: datetime
    updated_at: datetime

class CourseMemberOut(Schema):
    id: int 
    course_id: CourseSchemaOut
    user_id: UserOut
    roles: str
    # created_at: datetime


class CourseSchemaIn(Schema):
    name: str
    description: str
    price: int


class CourseContentMini(Schema):
    id: int
    name: str
    description: str
    course_id: CourseSchemaOut
    created_at: datetime
    updated_at: datetime


class CourseContentFull(Schema):
    id: int
    name: str
    description: str
    video_url: Optional[str]
    file_attachment: Optional[str]
    course_id: CourseSchemaOut
    created_at: datetime
    updated_at: datetime

class CourseCommentOut(Schema):
    id: int
    content_id: CourseContentMini
    member_id: CourseMemberOut
    comment: str
    created_at: datetime
    updated_at: datetime

class CourseCommentIn(Schema):
    comment: str

class UserEdited(Schema):
    first_name : str
    last_name : str
    email : str
    phone_number : str
    description : str
    profile_picture : str
    updated_at : datetime
    
class AnnouncementCreateSchema(Schema):
    course_id: int
    title: str
    content: str
    show_date: date
    created_by: str

class AnnouncementEditSchema(Schema):
    title: str
    content: str
    show_date: date

class AnnouncementResponseSchema(Schema):
    id: int
    course_id: int
    teacher_id: int
    title: str
    content: str
    date_posted: date
    show_date: date


class CompletionTrackingCreateSchema(Schema):
    student_username: str  # Username dari student
    content_id: int
    course_id: int# ID konten yang udah dikerjain
    
    
class CompletionTrackingResponseSchema(Schema):
    content_name: str  # Nama konten yang diselesaikan
    completed_at: datetime  # Waktu selesai
    completed: bool  # Status apakah udah selesai atau belum
    
class BookmarkRequestSchema(Schema):
    student_id: int
    content_id: int


class BookmarkResponseSchema(Schema):
    id: int
    student_id: int
    content_id: int
    content_name: str
    course_id: int
    course_name: str


