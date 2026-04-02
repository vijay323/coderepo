class ReportGenerator:
    def generate(self, data):
        pass

class PDFGenerator(ReportGenerator):
    def generate(self, data):
        print(f"Generating PDF report for {data}")

class ExcelGenerator(ReportGenerator):
    def generate(self, data):
        print(f"Generating Excel report for {data}")

class TextGenerator(ReportGenerator):
    def generate(self, data):
        print(f"Generating Text report for {data}")

def create_report(generator, data):
    generator.generate(data)

data = "Monthly Sales"

create_report(PDFGenerator(), data)
create_report(ExcelGenerator(), data)
create_report(TextGenerator(), data)