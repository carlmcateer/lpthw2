## This does not work

import xlwt
import xlrd

wkbk = xlwt.Workbook()
outsheet = wkbk.add_sheet('Sheet1')

xlsfiles = [r'test1.xlsx', r'test2.xlsx']

outrow_idx = 0
for f in xlsfiles:

    insheet = xlrd.open_workbook(f).sheets()[0]
    for row_idx in xrange(insheet.nrows):
        for col_idx in xrange(insheet.ncol):
            outsheet.write(outrow_idx, col_idx
                            insheet.cell_value(row_idx, col_idx))
        outrow_idx += 1

wkbk.save(r'merge.xlsx')
