from fpdf import FPDF
pdf = FPDF()
pdf.add_page() # add página
pdf.set_font('Arial', 'BI', 16)  # B negrito, I itálico
pdf.cell(40, 10, 'Olá Trouxas! hahaha') #Posição
pdf.output('3-Arquivos/exemplo.pdf')