
import os

from openpyxl import load_workbook
from openpyxl import Workbook

# 文言文件目录
rootdir = 'D:/HYRON_input_AI_190308/FZ-Application/xml'

# 外部参照的属性一览
pd = 'ProcItemDialog.'
unitAttribList = ['no','ident','isLoopStart','isLoopEnd','setEnable',\
        'getEnable','multiData','multiNum','multiCalc',\
        'analyzable','LowerDataIdent','UpperDataIdent','inputParam',\
        'outputParam','isGroup','isSubGroup','settingType','isAction']
# 外部参照的设定对话框
diagList = ['CalculationDialog','ColorDialog','ColorExtractDialog','FigureDialog',\
        'PointDialog','UnitSelectDialog','CommonDialog','ValueSetDialog','LimitSetDialog',\
        'ComboBoxDialog','NoDialog','FileDialog','FolderDialog','MultiLineTextDialog']
# 外部参照的设定对话框的设定属性一览
attrList = [\
    ['MaxLength'],\
    ['ThroughEnable','DisplaySubNo','DataIdentR','DataIdentG','DataIdentB',\
        'ColorRangeSupport','DataIdentGR','DataIdentGG','DataIdentGB','DataIdentColor',\
        'DataIdentColorG','ColorAreaFigNo'],\
    ['ThroughEnable','DisplaySubNo','AutoSetting','DataIdentUpperH','DataIdentLowerH',\
        'DataIdentUpperS','DataIdentLowerS','DataIdentUpperV','DataIdentLowerV','DataIdent'],\
    ['ThroughEnable','DisplaySubNo','FigureNo','FigureKind','FigureMax','CircleMode',\
        'LineArrowMode','NotOnlyFigureEnabled','OrNotEnabled','DeleteDisable',\
        'ActionType','ActionIdent','ActionValue'],\
    ['ThroughEnable','DisplaySubNo','DecimalPlaces','MaxX','MinX','MaxY','MinY','DataIdentX','DataIdentY'],\
    ['TargetScene','MaxUnitNo','MinUnitNo','ItemIdentFilters','CategoryFilters'],\
    ['MaxLength'],\
    ['DecimalPlaces','Max','Min','Interval'],\
    ['SliderEnable','DecimalPlaces','Max','Min','LargeChange','SmallChange',\
        'TickFrequency','Interval','DataIdentUppValue','DataIdentLowValue'],\
    ['MessageFileIdent','TextIdentList','ValueList'],\
    ['ActionType','ActionIdent','ActionValue'],\
    ['RootFolderIdent','MessageFileIdent','FilterMessage','ExSupportFolderList','ModeOpen','IsImage',\
        'IsLocalPC','IsMem','IsUSBMemory','PreviewEnabled','ShowLoggingImage','ShowRegisteredImage','ShowStandardImage'],\
    ['RootFolderIdent','ExSupportFolderList','IsImageFolder','IsLocalPC','IsMemFolder','IsUSBMemory','VisibleNewFolder'],\
    ['MaxLength']\
    ]

# 外部参照的设定对话框的词典
attrDict = dict(zip(diagList,attrList))

def make_csv_header():
    head1=[None]*(len(unitAttribList)+1)
    for key in attrDict:
        head1.append(key)
        head1 += [None]*(len(attrDict[key]) - 1)

    head2 = ['tag'] + unitAttribList
    for key in attrDict:
        head2 += attrDict[key]
    
    return [head1,head2]

def parseXMLbyElementTree(xmlfile):
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    
    # 外部参照的设定对话框属性个数列表
    diagAttrbLenList = list(map(lambda x:len(attrDict[x]),diagList))

    def getlen(x):
        '''
            计算指定的设定对话框属性的偏移位置
        '''
        offset = 0
        for idx in range(0,diagList.index(x)): 
            offset += diagAttrbLenList[idx]
        return offset

    # 外部参照的设定对话框属性的偏移位置列表
    diagAttrbOffList = list(map(getlen,diagList))

    # 解析XML文件
    tree = ET.parse(xmlfile)  # <class 'xml.etree.ElementTree.ElementTree'>
    root = tree.getroot()     # 获取根节点 <Element 'data' at 0x02BF6A80>
    # print(root.tag, ":", root.attrib) # 打印根元素的tag和属性
    unitdata = root[0]        # 获取unitdata节点
    # print(unitdata.tag, ":", unitdata.attrib) # 打印根元素的tag和属性
    
    err = False
    # lines = [make_csv_header()]
    lines = make_csv_header()
    for node in unitdata:
        # print('node={}'.format(node.tag))

        line = [node.tag]
        for attr in unitAttribList:
            line.append(node.attrib.get(attr,'%NULL%'))
            # print('--','{}={}'.format(attr,node.attrib.get(attr,'%NULL%')))

        for subnode in node:
            
            if subnode.tag == 'setting':
                settingType = subnode.attrib['Type'].split('.')[1]
                # print('----','Type={}'.format(pd + settingType))
                if settingType in diagList:
                    line[unitAttribList.index('settingType')+1] = settingType
                    line += [None]*diagAttrbOffList[diagList.index(settingType)]
                    # print('----','AttribPos={}'.format(offset))

                    for diagAttrs in attrDict[settingType]:
                        line.append(subnode.attrib.get(diagAttrs,'%NULL%'))
                        # print('----','{}={}'.format(diagAttrs,subnode.attrib.get(diagAttrs,'%NULL%')))
                else:
                    print('Type Error %s' % settingType)
                    err = True
                    break
        lines.append(line)

        if err: 
            lines = []
            break

    # print(lines)
    unit = os.path.basename(xmlfile).split('_')[0]
    return lines,unit
    # make_csv_file(lines,unit)

def make_csv_file(lines, unit_name):
    '''
        行list保存到CSV文件
    '''
    import csv

    dir = os.path.join(os.getcwd(), 'Result')
    if not os.path.isdir(dir):
        os.mkdir(dir)
    fn = os.path.join(dir,'{}.csv'.format(unit_name))

    # CSV
    with open(fn, 'w', encoding='UTF-8-sig', newline='') as fw:
        writer = csv.writer(fw)
        for line in lines:
            writer.writerow(line)

def make_workbook_sheet(wb,lines, unit_name):

    if len(unit_name) > 31: unit_name = unit_name[0:31]
    ws = wb.create_sheet(unit_name)

    for line in lines:
        ws.append(line)

def get_xmlfile_list():
    '''
        根据语言索引取得单一语言的文件一览
    '''
    import glob # 文件名模式匹配库
    filelist = glob.glob(os.path.join(rootdir,'*_UnitData.xml'))
    return filelist

def process_filelist(filelist):
    '''
        处理所有XML文件
    '''
    # 创建一个工作表
    wb = Workbook()
    # 删除默认sheet
    sheet = wb.active
    wb.remove(sheet)

    err_units = []
    for name in filelist:
        # print('{} start'.format(name))
        lines,unit = parseXMLbyElementTree(name)
        # make_csv_file(lines,unit)        
        if len(lines) == 0: err_units.append(unit)
        
        make_workbook_sheet(wb,lines,unit)
        print('{} finished'.format(os.path.basename(name)))

    # 保存xlsx文件
    dir = os.path.join(os.getcwd(), 'Result')
    if not os.path.isdir(dir):
        os.mkdir(dir)
    fn = os.path.join(dir,'xml2xlsx.xlsx')
    wb.save(fn)
    print('{} saved'.format(os.path.basename(fn)))
    print('all error units: \n', err_units)

def xml2xlsx():
    process_filelist(get_xmlfile_list())

def main():
    """
        主函数
    """
    xml2xlsx()

if __name__ == '__main__':
    main()
