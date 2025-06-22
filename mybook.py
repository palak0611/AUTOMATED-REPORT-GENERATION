from fpdf import FPDF

title='SOFTWARE ENGINEERING'

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica','B',15)
        title_w=self.get_string_width(title)+6
        doc_w=self.w
        self.set_x((doc_w-title_w)/2)
        self.set_draw_color(0,80,100)
        self.set_fill_color(230,230,0)
        self.set_text_color(220,50,50)
        self.set_line_width(1)
        self.cell(title_w,10,title,border=1,ln=1,align='C',fill=-1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',8)
        self.set_text_color(169,169,169)
        self.cell(0,10,f'Page{self.page_no()}',align='C')

    def chapter_title(self,ch_num,ch_title):
        self.set_font('helvetica','',12)
        self.set_fill_color(200,220,255)
        chapter_title=f'Chapter{ch_num}:{ch_title}'
        self.cell(0,5,chapter_title,ln=1,fill=1)
        self.ln()

    def chapter_body(self,name):
        with open(name,'rb') as fh:
            txt=fh.read().decode('latin-1')
            self.set_font('times','',12)
            self.multi_cell(0,5,txt)
            self.ln()
            self.set_font('times','I',12)
            self.cell(0,5,'END OF CHAPTER')

    
    def print_chapter(self,ch_num,ch_title,name):
        self.add_page()
        self.chapter_title(ch_num,ch_title)
        self.chapter_body(name)

pdf=PDF('P','mm','Letter')
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto = True, margin = 15)
pdf.add_page()
pdf.image('background_image.PNG', x = -0.5, w = pdf.w + 1)
pdf.print_chapter(1, 'INTODUCTION TO SOFTWARE ENGINEERING', 'chp1.txt.')
pdf.print_chapter(2, 'SOFTWARE REQUIREMENT ANALYSIS', 'chp2.txt')
pdf.output('S.E.pdf')