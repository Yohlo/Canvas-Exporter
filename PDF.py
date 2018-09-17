from pdfrw import PdfReader, PdfWriter
import pdfrw

def split(fname, names, folder, pages=1):
    """
    This function splits a big pdf into individual ones and names them 
    in the order given in a txt files. This function relies on the pdfrw library.

    Disclaimer: I have not tested this function on quizzes with multiple pages :)

    Args:
        fname (str):            Path to the large PDF to split. 
        names (str):            Path to a txt file containing the order in which to name the files
        folder (str, optional): Folder to save the new PDFs in. 
        pages (int, optional):  Number of pages to include in the smaller PDFs

    Returns: 
        This function does not return anything. 
    """

    with open(names) as f:
        lines = f.readlines()
        lines = [x.split(" ")[0].strip() for x in lines]
    
    infile = PdfReader(fname)
    page_num = 1
    student = 0
    for i in range(len(infile.pages)):
        out = PdfWriter()
        if page_num < pages:
            out.addpage(infile.pages[i])
            page_num += 1
        else:
            out.addpage(infile.pages[i])
            out.write("%s%s.pdf" % (folder, lines[student]))
            page_num = 1
            student += 1

def merge(pdfs, output): 
    """
    This function takes a list of PDFs and merges them into one PDF, in the order they are in the list.

    Args:
        pdfs (list of str): List of paths to PDF files to merge
        output (str):       Path to save the the merged PDF to. 
    
    Returns:
        This function does not return anything
    """    

    out = pdfrw.PdfWriter()

    for pdf in pdfs:
        inf = pdfrw.PdfReader(pdf)
        for i in range(len(inf.pages)):
            out.addpage(inf.pages[i])
    
    out.write(output)