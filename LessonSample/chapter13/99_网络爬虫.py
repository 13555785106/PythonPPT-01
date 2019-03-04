#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import sqlite3
import urllib2
import urlparse

from lxml import etree

count = 0

start_urls = [
    "http://www.iconarchive.com/category/alphabet-icons.html",
    "http://www.iconarchive.com/category/cartoon-icons.html",
    "http://www.iconarchive.com/category/halloween-icons.html"]

conn = sqlite3.connect('sqlite3.1.db')
print "数据库打开成功!"
"""
conn.execute('''CREATE TABLE IF NOT EXISTS urls
       (url VARCHAR(512) PRIMARY KEY NOT NULL,
       crawled BOOLEAN,
       grabbedTime DATETIME);''')
conn.execute("DELETE FROM urls;")
conn.commit()
for url in start_urls:
    conn.execute("INSERT INTO urls (url,crawled,grabbedTime) VALUES(?,?,?)",
                 (url, False, datetime.datetime.now()))

conn.commit()
"""
while True:
    rows = conn.execute("SELECT * FROM urls WHERE crawled = ?", (0,)).fetchmany(10)
    if len(rows) == 0:
        break
    for row in rows:
        url = row[0]
        conn.execute("UPDATE urls SET crawled=1 WHERE url=?", (url,))
        conn.commit()
        count = count + 1
        print url, count
        try:
            response = urllib2.urlopen(url, timeout=15)
            html = response.read()
            html_tree = etree.HTML(html)
            for href in html_tree.xpath("//a/@href"):
                if href.endswith(".html") and not href.startswith("http"):
                    href = urlparse.urljoin(url, href)

                if href.startswith("http://www.iconarchive.com/") and href.endswith(".html") and \
                        conn.execute("SELECT count(*) FROM urls WHERE url=?", (href,)).fetchone()[0] == 0:
                    conn.execute(
                        "INSERT INTO urls (url,crawled,grabbedTime) VALUES(?,?,?)",
                        (href, False, datetime.datetime.now()))
            conn.commit()
        except Exception as e:
            print e

conn.close()
print "数据库关闭成功!"
