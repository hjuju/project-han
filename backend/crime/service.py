from common.services import Printer, Reader
from common.models import FileDTO


class CrimeService(Printer, Reader):
    printer = Printer()
    reader = Reader()
    file = FileDTO()

    def csv(self, payload):

        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.csv(self.file))

    def xls(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.xls(self.file))

    def json(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.json(self.file))

    def new_file(self):
        pass


