

from xml import sax


# xmlfile='D:\\GitHub\\LearnPython\\Learn\\XML\\FilterAdvanced_UnitData.xml'
xmlfile='D:\\GitHub\\LearnPython\\Learn\\XML\\Search2_UnitData.xml'
    

xmlstr = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

class MySaxHandler(sax.ContentHandler):
    def startElement(self, name, attrs):
        '''
            重写基类函数
        '''
        # print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
        print('sax:start_element: %s' % name)
        self.print_attrs(attrs)

    def endElement(self, name):
        '''
            重写基类函数
        '''
        print('sax:end_element: %s' % name)

    def characters(self, text):
        '''
            重写基类函数
        '''
        print('sax:char_data: %s' % text)

    def print_attrs(self, attrs):
        for key,value in attrs.items():
            print('  {}="{}"'.format(key , value))

def test_SAX_1():
    # 解析XML字符串
    import xml.parsers
    import xml.parsers.expat

    parser=xml.parsers.expat.ParserCreate()
    handler = MySaxHandler()
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    # parser.Parse(xmlstr)
    # 也可解析XML文件
    parser.ParseFile(open(xmlfile,'rb'))


def test_SAX_2():
    # 解析XML文件
    xml_parser = sax.make_parser()
    # 关闭命名空间
    xml_parser.setFeature(sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    handler = MySaxHandler()
    xml_parser.setContentHandler(handler)
    xml_parser.parse(xmlfile)


def test_DOM():
    '''
        已知XML结构的情况下用DOM
    '''
    import xml.dom.minidom

    dom = xml.dom.minidom.parse(xmlfile)  #打开xml文档
    root = dom.documentElement            #得到xml文档对象
    print(root)
    print("nodeName:", root.nodeName)        #每一个结点都有它的nodeName，nodeValue，nodeType属性
    print("nodeValue:", root.nodeValue)      #nodeValue是结点的值，只对文本结点有效
    print("nodeType:", root.nodeType)
    print("ELEMENT_NODE:", root.ELEMENT_NODE)

    root2 = root.getElementsByTagName('UNITDATA') # 返回符合条件的节点列表
    print(root2)
    print("nodeName:", root2[0].nodeName)      
    print("nodeValue:", root2[0].nodeValue)    
    print("nodeType:", root2[0].nodeType)
    print("ELEMENT_NODE:", root2[0].ELEMENT_NODE)

# 文言文件目录
rootdir = 'D:/HYRON_input_AI_190308/FZ-Application/xml'

# 外部参照的属性一览
pd = 'ProcItemDialog.'
unitAttribList = ['no','ident','isLoopStart','isLoopEnd','setEnable',\
        'getEnable','multiData','multiOffset','multiNum','multiCalc',\
        'analyzable','LowerDataIdent','UpperDataIdent','inputParam',\
        'outputParam','isGroup','isSubGroup','settingType','isAction']
# 外部参照的设定对话框
diagList = ['CalculationDialog','ColorDialog','ColorExtractDialog','FigureDialog',\
        'PointDialog','UnitSelectDialog','CommonDialog','ValueSetDialog','LimitSetDialog',\
        'ComboBoxDialog','NoDialog','FileDialog','FolderDialog']
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
    ['RootFolderIdent','MessageFileIdent','FilterMessage','ExSupportFolderList',\
        'ModeOpen','IsImage','IsLocalPC','IsMem','IsUSBMemory','PreviewEnabled','ShowLoggingImage','ShowStandardImage'],\
    ['RootFolderIdent','ExSupportFolderList','IsImageFolder','IsLocalPC','IsMemFolder','IsUSBMemory','VisibleNewFolder']\
    ]

# 外部参照的设定对话框的词典
attrDict = dict(zip(diagList,attrList))

import os

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
                    line += [None]*diagAttrbOffList[diagList.index(settingType)]
                    # print('----','AttribPos={}'.format(offset))

                    for diagAttrs in attrDict[settingType]:
                        line.append(subnode.attrib.get(diagAttrs,'%NULL%'))
                        # print('----','{}={}'.format(diagAttrs,subnode.attrib.get(diagAttrs,'%NULL%')))
                else:
                    print('Type Error')
                    err = True
                    break
        if err: break
        lines.append(line)
    # print(lines)
    unit = os.path.basename(xmlfile).split('_')[0]
    make_csv_file(lines,unit)

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
   
    for name in filelist:
        print('{} start'.format(name))
        parseXMLbyElementTree(name)
        print('{} finished'.format(os.path.basename(name)))

def test():
    # parseXMLbyElementTree()
    process_filelist(get_xmlfile_list())

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()