if __name__ == "__main__":

    start_date = '2020-01-01'
    end_date = '2021-07-14'
    os.chdir('C:\\Users\\shic\\Desktop\\Project\\ind_report')
    filepath = os.getcwd()+'\\'
    pdfpath = filepath+'pdf'
    txtpath = filepath+'text'
    if not os.path.exists(filepath):
        os.mkdir(filepath);os.mkdir(pdfpath);os.mkdir(txtpath)

    ### crawling
    df_excel = naver_crawler_ind(crpname, start_date, end_date)

    ### download pdf
    pdf_download(df_excel['pdf'], pdfpath)

    ### read text in pdf
    # multi processing
    pool = multiprocessing.Pool(processes=2)
    pool.map(pdfread, (filepath,))
    pool.close()
    pool.join()

    ### text preprocessing: extract text
    pdf_list = extract_txt(txtpath)

    print("Total <%d> Files"%len(os.listdir('data/'+crpname+'/text')))

    ### save text
    df_excel = pd.merge(df_excel, pdf_list, how = 'outer' )

    writer = pd.ExcelWriter(filepath+crpname+'_report_text.xlsx')
    df_excel.to_excel(writer, 'Sheet1', index = False)
    writer.save() 