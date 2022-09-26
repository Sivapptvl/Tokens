import fitz
from threading import Thread



###########################################
# Thread Class to make pdf page from images

class MakePDFPage(Thread) :

    def __init__(self, n) :
        Thread.__init__(self)
        self.page_no = n
        self.pdf = None

    def run(self) :

        page = fitz.open(f"{SOURCE_DIR}page{self.page_no:02d}.png")  # opening an image
        page_to_pdf = page.convert_to_pdf()  # converting image to pdf page

        self.pdf = page_to_pdf




#####     OUTPUT EMPTY FILE     #####
OUTPUT = fitz.open()  # empty pdf file




###############################
# Creates pdf pages from images

def create_pages(start, end) :
    
    Pages = ()

    for page_no in range(start, end + 1) :

        page = MakePDFPage(page_no)
        Pages += (page, )
        page.start()

    return Pages




#####################################
# Inserts the pages into the PDF File

def insert_pages(Pages) :

    for page in Pages : 
    
        page.join()  # Waits for threads to complete

    pg_no = 0
    
    for page in Pages :    
        
        pg_no += 1

        pdf = fitz.open("pdf", page.pdf)   # opening the converted pdf page
        OUTPUT.insert_pdf(pdf)    # Adding page to OUTPUT file

        print(f"Inserted Page {pg_no:02d}")

    OUTPUT.save(f"{OUTPUT_DIR}{OUTPUT_NAME}.pdf")

    print("-"*17)
    print("COMPLETED PROCESS")
    print("-"*17)



####################
# Information Inputs

SOURCE_DIR = "PageThread\\"

OUTPUT_DIR = ""
OUTPUT_NAME = "Tokens"



############################################################

t = create_pages(1, 25)   # Create Pages from image 1 to image 15
insert_pages(t)