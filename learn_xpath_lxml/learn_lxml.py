from lxml import html

etree = html.etree


def parse_text():
    html_str = ''
    with open('伯乐在线.html', 'r', encoding='utf-8') as fp:
        html_str = fp.read()

    # 生成html对象
    html_el = etree.HTML(html_str)
    print(etree.tostring(html_el, encoding='utf-8').decode('utf-8'))


def parse_file():
    # 使用html解析器
    parser = etree.HTMLParser(encoding='utf-8')

    # 解析html
    html_el = etree.parse('伯乐在线.html', parser=parser)
    print(etree.tostring(html_el, encoding='utf-8').decode('utf-8'))


def learn_xpath_lxml():
    parser = etree.HTMLParser(encoding='utf-8')
    html_el = etree.parse('伯乐在线.html', parser=parser)

    # 获取所有a标签
    el_list = html_el.xpath('//a')
    for el in el_list:
        print(etree.tostring(el, encoding='utf-8').decode('utf-8'))

    # 获取第二个a标签
    el_2 = html_el.xpath('//a[2]')[0]
    print(etree.tostring(el_2, encoding='utf-8').decode('utf-8'))

    # 根据属性筛选
    el_3 = html_el.xpath('//img[@alt="返回顶部"]')
    print(el_3)

    # 提取出节点的属性
    el4 = html_el.xpath('//a/@href')
    for href in el4:
        print(href)

    # 获取纯文本
    el5 = html_el.xpath('//a/text()')
    for t in el5:
        print(t)


if __name__ == '__main__':
    # parse_text()
    # parse_file()
    learn_xpath_lxml()
