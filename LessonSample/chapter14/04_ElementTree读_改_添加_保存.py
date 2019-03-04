#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('movies.xml')
print dir(tree)

root = tree.getroot()
print root.attrib['shelf']
for item in root:
    print "---------------------------"
    print 'Title:', item.attrib['title']
    # print dir(item)
    for ci in item.getchildren():
        print ci.tag.capitalize() + ":" + ci.text

root.set('description', unicode('简单描述', 'UTF-8'))
element = xml.etree.ElementTree.SubElement(root, 'movie')
element.attrib['title'] = u'无极'
xml.etree.ElementTree.SubElement(element, 'type').text = u'古装、神剧'
xml.etree.ElementTree.SubElement(element, 'year').text = '2007'
xml.etree.ElementTree.SubElement(element, 'format').text = 'VHS'
xml.etree.ElementTree.SubElement(element, 'rating').text = 'PG'
xml.etree.ElementTree.SubElement(element, 'stars').text = '5'
xml.etree.ElementTree.SubElement(element, 'description').text = u'陈凯歌神剧'

tree.write('movies01.xml', encoding='UTF-8')
