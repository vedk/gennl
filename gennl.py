#!/usr/bin/env python3
title = []
date = []
link = []
imgsrc = []
desc = []
meme = []

# edit the following to change content
# 0
title.append('The Taliban won Afghanistan\'s technological war')
link.append('https://www.technologyreview.com/2021/08/23/1032459/afghanistan-taliban-war-technological-progress/')
imgsrc.append('https://wp.technologyreview.com/wp-content/uploads/2021/08/AP_21231367404369.jpg?fit=2064,1376')
desc.append('It was the Taliban that gained most from technological progress.')
date.append('Aug 23, 2021')

# 1
title.append('30 years of Linux: OS was successful because of how it was licensed, says Red Hat')
link.append('https://www.theregister.com/2021/08/25/30_years_of_linux_red_hat/')
imgsrc.append('https://regmedia.co.uk/2021/08/25/redhat.jpg')
desc.append('Now Google reckons security isn\'t good enough, and Android is proprietary')
date.append('Aug 25, 2021')

# 2
title.append('The Semiconductor Heist Of The Century')
link.append('https://semianalysis.substack.com/p/the-semiconductor-heist-of-the-century')
imgsrc.append('https://bit.ly/3jmwyEo')
desc.append('Arm China Has Gone Completely Rogue.')
date.append('Aug 27, 2021')

# 3
title.append('Spies for Hire')
link.append('https://bit.ly/3zsX3xk')
imgsrc.append('https://img.etimg.com/thumb/msid-85678412,width-300,imgsize-30538,,resizemode-4,quality-100/.jpg')
desc.append('China\'s new breed of hackers blends espionage and entrepreneurship')
date.append('Aug 27, 2021')

# 4
title.append('19 Lessons From the Software Industry')
link.append('https://www.business2community.com/strategy/19-pandemic-era-lessons-from-the-software-development-industry-02426076')
imgsrc.append('https://top.studio/wp-content/uploads/2020/03/b2c-marketing-what-does-work-in-2020.jpg')
desc.append('Compared to other industries blindsided by the pandemic...')
date.append('Aug 18, 2021')

# 5
title.append('Critical Cosmos Database Flaw')
link.append('https://thehackernews.com/2021/08/critical-cosmos-database-flaw-affected.html')
imgsrc.append('https://d13uzbxp4vxmou.cloudfront.net/wp-content/uploads/2019/05/cosmos-db-200x177px.png')
desc.append('This affected thousands of Microsoft Azure Customers')
date.append('Aug 27, 2021')


meme.append('https://i.redd.it/5mgkku4m92k71.jpg')
meme.append('https://i.redd.it/yn1pu5cu8zj71.png')
meme.append('https://i.redd.it/3nzu3smytyj71.jpg')


wncc_update_imgsrc = ''
wncc_update_desc = 'Abc'


data = {
    'title0': title[0], 'link0': link[0], 'imgsrc0': imgsrc[0], 'desc0': desc[0], 'date0': date[0],
    'title1': title[1], 'link1': link[1], 'imgsrc1': imgsrc[1], 'desc1': desc[1], 'date1': date[1],
    'title2': title[2], 'link2': link[2], 'imgsrc2': imgsrc[2], 'desc2': desc[2], 'date2': date[2],
    'title3': title[3], 'link3': link[3], 'imgsrc3': imgsrc[3], 'desc3': desc[3], 'date3': date[3],
    'title4': title[4], 'link4': link[4], 'imgsrc4': imgsrc[4], 'desc4': desc[4], 'date4': date[4],
    'title5': title[5], 'link5': link[5], 'imgsrc5': imgsrc[5], 'desc5': desc[5], 'date5': date[5],

    'meme0': meme[0], 'meme1': meme[1], 'meme2': meme[2],

    'wncc_update_imgsrc': wncc_update_imgsrc, 'wncc_update_desc': wncc_update_desc
}


with open('index.html', 'r', encoding='utf-8') as fd:
    html = fd.read()

# the <head> of the template contains '{' characters, so we can't use
# str.format() directly
head, body = html.split('||')

with open('out.html', 'w', encoding='utf-8') as fd:
    fd.write(head + body.format(**data))
