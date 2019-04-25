
# import xml.sax.xmlreader
from xml import sax


xmlfile='D:\\GitHub\\LearnPython\\Learn\\XML\\Search_UnitData.xml'

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

def test_SAX():
    ''' 解析XML字符串
    import xml.parsers
    import xml.parsers.expat

    parser=xml.parsers.expat.ParserCreate()
    handler = MySaxHandler()
    # parser.setContentHandler(handler)
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    parser.Parse(xmlstr)
    # 解析XML文件
    parser.ParseFile(open(xmlfile,'rb'))
    '''

    # 解析XML文件
    xml_parser = sax.make_parser()
    # 关闭命名空间
    xml_parser.setFeature(sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    handler = MySaxHandler()
    xml_parser.setContentHandler(handler)
    xml_parser.parse(xmlfile)

def main():
    """
        主函数
    """
    test_SAX()

if __name__ == '__main__':
    main()