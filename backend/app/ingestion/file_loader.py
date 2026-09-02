from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption


def load_txt_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text

pipeline_options = PdfPipelineOptions()
pipeline_options.do_formula_enrichment = True

def load_pdf_file(file_path: str) -> str:

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options
            )
        }
    )

    result = converter.convert(file_path)

    text = result.document.export_to_markdown()

    return text