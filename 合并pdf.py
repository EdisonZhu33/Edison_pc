import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # 打开两个PDF文件
    with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
        # 创建PDF阅读器对象
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        pdf2_reader = PyPDF2.PdfReader(pdf2_file)

        # 创建PDF写入器对象
        pdf_writer = PyPDF2.PdfWriter()

        # 将第一个PDF的所有页面添加到写入器中
        for page in pdf1_reader.pages:
            pdf_writer.add_page(page)

        # 将第二个PDF的所有页面添加到写入器中
        for page in pdf2_reader.pages:
            pdf_writer.add_page(page)

        # 将合并后的PDF写入输出文件
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


# 用两个PDF文件的路径替换以下占位符
pdf1_path = 'C:\\Users\\zhucheng\\Desktop\\赣南科技学院报名\\毕业证.pdf'
pdf2_path = 'C:\\Users\\zhucheng\\Desktop\\赣南科技学院报名\\学位证.pdf'

# 指定合并后的PDF输出路径
output_path = 'C:\\Users\\zhucheng\\Desktop\\赣南科技学院报名\\本科毕业加学位证.pdf'

# 调用函数，合并PDF文件
merge_pdfs(pdf1_path, pdf2_path, output_path)
