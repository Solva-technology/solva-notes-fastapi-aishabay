from app.db.crud.base import CRUDBase
from app.db.models import Note


class CRUDNote(CRUDBase):
    pass


note_crud = CRUDBase(Note)
