# from pydantic import BaseModel
# from datetime import datetime

# class NotificationBase(BaseModel):
#     id: str
#     title: str
#     message: str
#     status: str

# class NotificationCreate(NotificationBase):
#     pass

# class NotificationRead(NotificationBase):
#     id: str
#     created_at: datetime
#     updated_at: datetime
#     class Config:
#         orm_mode = True