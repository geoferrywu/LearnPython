

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
    print(root.childNodes)
    print("nodeName:", root.nodeName)        #每一个结点都有它的nodeName，nodeValue，nodeType属性
    print("nodeValue:", root.nodeValue)      #nodeValue是结点的值，只对文本结点有效
    print("nodeType:", root.nodeType)
    print("ELEMENT_NODE:", root.ELEMENT_NODE)

    root2 = root.getElementsByTagName('UNITDATA') # 返回符合条件的节点列表
    
    print("nodeName:", root2[0].nodeName)      
    print("nodeValue:", root2[0].nodeValue)    
    print("nodeType:", root2[0].nodeType)
    print("ELEMENT_NODE:", root2[0].ELEMENT_NODE)
    
    print(root2[0].childNodes)

    for node in root2[0].childNodes:
        if node.nodeType==1:
            print(node.nodeName,node.attributes)

    # with open('d:\\dom_write.xml','w',encoding='UTF-8',newline='') as fh:
    #         dom.writexml(fh,indent='',addindent='  ',newl='',encoding='UTF-8')


def test_elementTree():
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET

    # 解析XML文件
    tree = ET.parse(xmlfile)  # <class 'xml.etree.ElementTree.ElementTree'>
    root = tree.getroot()     # 获取根节点 <Element 'data' at 0x02BF6A80>
    # print(root.tag, ":", root.attrib) # 打印根元素的tag和属性
    unitdata = root[0]        # 获取unitdata节点
    # print(unitdata.tag, ":", unitdata.attrib) # 打印根元素的tag和属性
    node = unitdata[0]
    print(node.tag, ":", node.attrib) # 打印根元素的tag和属性
    node.attrib ={}

    tree.write('d:\\out.xml')


def test_new_xml():
    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET

    # root = ET.ElementTree('Reference')
    root = ET.Element('Reference')
    root.text = '\n  '
    unitdata = ET.SubElement(root,'UNITDATA', {})
    unitdata.text = '\n    '
    unitdata.tail = '\n'
    node=ET.SubElement(unitdata,'model',{'name':'model'})
    node.tail = '\n  '
    # root.append(unitdata)
    tree=ET.ElementTree(root)

    tree.write('d:\\out.xml',encoding='UTF-8',xml_declaration=True)
    
    
def test():
    test_new_xml()

def main():
    """
        主函数
    """
    test()

if __name__ == '__main__':
    main()
