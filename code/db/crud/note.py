from code.db.crud.base import CRUDBase
from code.db.models import Note


class CRUDNote(CRUDBase):
    pass


note_crud = CRUDBase(Note)
