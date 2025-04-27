import os
import string

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LAParams
from string_parser import processa_string


def processa_pdf(path_pdfs: string):
    for file in os.listdir(path_folder_pdfs):
        if file.endswith(".pdf"):
            path_pdf = f"{path_folder_pdfs}\\{file}"
            path_pdfs_processados = path_pdf.replace("pdfs", "pdfs_processados").replace(" ", "-").replace(".pdf",
                                                                                                           ".txt")
            with open(path_pdfs_processados, "w", encoding="utf-8") as arquivo:
                print(f"\rProcessando: {path_pdf} > {path_pdfs_processados}")
                for i, page_layout in enumerate(extract_pages(path_pdf, laparams=LAParams()),start=1):
                    for element in page_layout:
                        if isinstance(element, LTTextContainer):
                            text = element.get_text()
                            if text and text.strip():
                                arquivo.write(processa_string(text))



if __name__ == '__main__':
    try:
        path_folder_pdfs = "pdfs"
        print("Iniciando processamento dos pdfs...")
        processa_pdf(path_folder_pdfs)
        print("finalizado!!!")
    except Exception as e:
        print(f"\n Ocorreu um erro durante a execução: {e}")
