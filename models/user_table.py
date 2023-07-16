from sqlalchemy import Column, String, Integer, Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User_Registration_form(Base):
    __tablename__ = "user_registration"
    name = Column("username", String(50), primary_key=True)
    fname = Column("firstname", String(100))
    lname = Column("lastname", String(50))
    date = Column("dob", Date)
    password = Column("password", VARCHAR)
    cpassword = Column("confirm_password", VARCHAR)
    mail = Column("email_id", VARCHAR)
    ph_no = Column("phone_no", Integer)
    address = Column("address", VARCHAR)
    category = Column("category", String)
