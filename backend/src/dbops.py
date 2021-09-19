from .database import engine
from sqlmodel import Session, select
from .models import Highlight, Page, AnnotationDB
from uuid import UUID
from pydantic import AnyUrl


# from sqlmodel import SQLModel, create_engine

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

# engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

###########################################################
#### Page
###########################################################


def create_page(page: Page):

    with Session(engine) as session:

        session.add(page)
        session.commit()


def read_page(url: AnyUrl):

    with Session(engine) as session:
        statement = select(Page).where(Page.url == url)
        result = session.exec(statement).one()

        return result


## Update - NOTE not required
## Delete - NOTE not required

###########################################################
#### Highlights
###########################################################


## Create
def create_highlight(highlight: Highlight):
    with Session(engine) as session:

        session.add(highlight)
        session.commit()


## Read
def read_highlights(pageUrl: AnyUrl):
    """Return all highlights associated with the pageId."""
    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.pageUrl == pageUrl)
        results = session.exec(statement)

        return [x for x in results]


## Update
## NOTE not required

## Delete
def delete_highlight(id: UUID):

    with Session(engine) as session:
        statement = select(Highlight).where(Highlight.id == id)
        result = session.exec(statement).one()

        session.delete(result)
        session.commit()


###########################################################
#### AnnotationBase
###########################################################


def create_annotation(annotationDb: AnnotationDB):

    with Session(engine) as session:

        session.add(annotationDb)
        session.commit()


def read_annotations(pageUrl):

    with Session(engine) as session:
        statement = select(AnnotationDB).where(AnnotationDB.pageUrl == pageUrl)
        results = session.exec(statement)

        return [r for r in results]


## TODO Update
def update_annotation(id):
    pass


## TODO Delete
def delete_annotation(id):
    pass
