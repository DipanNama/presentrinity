from datetime import datetime
import random 

# get random value from 0 to 1
def get_random_value():
    return random.randint(0, 1)

# defining the contents 
contents = ''

# generate toc contents
toc_titles = []
def generate_toc():
  f3 = open('ai-generated.md', 'r+')
  while True:
      line = f3.readline()
      if not line:
        break
      if line.startswith('<<TOC>>'):
        formatted_toc = "\n".join(f"- {title}" for title in toc_titles)
        print(formatted_toc)
        f3.writelines(formatted_toc)
        f3.close()
        break

    # f.close()
    # f2 = open('ai-generated.md', 'w')
    # f2.writelines(formatted_toc)
    # f2.close()
  # return formatted_toc

# Define dynamic values
topic = "Artificial Intelligence"
name = "Dipan Nama"
student_id = "23IUT0030005"
branch = "MCA"
current_date = datetime.now().strftime("%b %d, %Y")
image_url = "https://www.medianama.com/wp-content/uploads/2024/06/ai-8529399_1920.jpg"

# Define types of slides
# slide_types = {
#     '*': 'bullet_points',
#     '-': 'bullet_points',
#     '```': 'code',
#     '```mermaid': 'diagram',
# }

slide_side = ['image-left', 'image-right']

# image_side = slide_side[get_random_value()]

# To show Slide number
page_no = '''
<div style="position: absolute; top: 20px; right: 20px; font-size: 0.6em; color: #4ad46e;">
  <code>
    <SlideCurrentNo /> / <SlidesTotal />
  </code>
</div>
'''

# To show Horizontal line
hr_line = "<hr style='border: 0; height: 2px; background: linear-gradient(to right, #ff7e5f, #feb47b); margin: 20px 0;' />"

# Define the structure of the markdown file
slideStructure = f'''---
theme: dracula
title: {topic}
hideInToc: true
info: |
  # Project Info
class: text-center
drawings:
  persist: false
transition: fade-out
mdc: true
overviewSnapshots: true
aspectRatio: 16/9
canvasWidth: 980
---
'''

# Template with placeholders
titleSlide = f'''
## {topic}

`The ICFAI University, Tripura`

<div class="pt-8">
  <span class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10" v-mark="{{ at: 1, color: 'red', type: 'underline' }}">
    Presented by <code>{name}</code>
  </span>
</div>

<div style="position: absolute; bottom: 50px; left: 50px; font-size: 0.8em; color: #4ad46e;">
  <code>Branch: {branch}</code>
  <br/>
  <code>{student_id}</code>
  <br/>
  <code>{current_date}</code>
</div>
'''

toc = f'''
---
layout: image-right
transition: fade-out
layoutClass: gap-16
image: https://mycvcreator.com/administrator/postimages/64a7c4a7005ed1.20845803.jpg
---

## Table of contents

{hr_line}

  <Toc
  minDepth="1" 
  maxDepth="2" 
  listClass='' 
  mode="all"
></Toc>

'''

# temp data for bullet points
# slide_title = 'AI Applications'
# bullet_points = '''
# - AI in Healthcare
# - AI in Education
# - AI in Finance
# - AI in Agriculture
# - AI in Transportation
# - AI in Entertainment
# - AI in Cybersecurity
# - AI in Retail
# '''
# image_side = 'image-right'

# Slide layouts for bullet points
bullet_points_slide = '''
--- 
transition: fade-out
layout: {image_side}
title: {slide_title}
image: {image_url}
---

## {slide_title}

{hr_line}

{page_no}

<v-clicks class="text-sm text-slate-400">

{bullet_points}

</v-clicks>
'''

# temp data for normal slide
# slide_title = 'AI in Healthcare'
# content = '''
# Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence.
# AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.
# '''
# image_side = 'image-left'

# Slide layouts for paragraph text or code
normal_slide= '''
---
transition: fade-out
layout: {image_side}
title: {slide_title}
image: {image_url}
---

## {slide_title}

{hr_line}

{page_no}

<p style="font-size:0.7em;"
  class="text-slate-400 tracking-wide text-justify"
  v-click
>

{content}
</p>
'''

# temp data
slide_title = "Introduction"
introduction_content_1 = 'Artificial intelligence (AI) is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence.'
introduction_content_2 = 'AI is an interdisciplinary science with multiple approaches, but advancements in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry.'

# introduction slide
introductionSlide = f'''
---
transition: fade-out
layout: image-right
title: Introduction
image: {image_url}
---

#{slide_title}

{hr_line}

{page_no}

<p style="font-size:0.7em;"
  class="text-slate-400 tracking-wide text-justify"
  v-click
  v-motion
  :initial="{{ y: 180 }}"
  :enter="{{ y: 0 }}"
  :leave="{{ y: 80 }}">

{introduction_content_1}
</p>

<p style="font-size:0.7em;"
  class="text-slate-400 tracking-wide text-justify"
  v-click
  v-motion
  :initial="{{ y: 180 }}"
  :enter="{{ y: 0 }}"
  :leave="{{ y: 80 }}">

{introduction_content_2}
</p>
'''

# Apply the formatting
# formatted_structure = slideStructure.format(topic=topic)
# print(formatted_structure)
# formatted_slide = titleSlide.format(topic=topic,name=name, id=student_id, branch= branch,date=current_date)

# formatted toc slide
# formatted_toc = toc.format(hr_line=hr_line)

# Remaining slides
remainingSlides = ''''''

# Read the content of the file
f = open('ai.md', 'r')
i = 1
while True:
    line = f.readline()
    if not line:
        break
    # print(line)
    if line.startswith(f'[slide {i}]'):
        # print('######slide-starting######')
        # print(i)
        next_line = f.readline()
        # print(next_line)
        toc_titles.append(next_line.split('#')[1].strip())
        slide_title = next_line.split('#')[1].strip()
        print(slide_title)
        while True:
            # lines = [line.strip() for line in f.readlines() if line.strip()]
            # for line in lines:
            #   print(line)
            if not line:
              break
            line = f.readline()
            if line.startswith(f'[slide {i}]'):
                i += 1
                # print('######slide-ending######')
                break
            # print("---line-data---")
            # if line.startswith('#'):
                # print("###title###")
                # print(line)
                
            elif not line:
                break
            else:
                # print("###content###")
                # print(line)
                contents += line
        # print(contents, end='')

        contents = "\n".join(line for line in contents.splitlines() if line.strip())
        # print(non_blank_lines)

        if contents.startswith('-'):
            # print("###bullet-points-slide###")
            bullet_points = bullet_points_slide.format(slide_title=slide_title, bullet_points=contents, image_side=slide_side[get_random_value()], image_url=image_url, hr_line=hr_line, page_no=page_no)
            # print(bullet_points)
            remainingSlides += bullet_points
            contents = ''
        
        if contents.startswith('*'):
            # print("###bullet-points-slide###")
            bullet_points = bullet_points_slide.format(slide_title=slide_title, bullet_points=contents, image_side=slide_side[get_random_value()], image_url=image_url, hr_line=hr_line, page_no=page_no)
            # print(bullet_points)
            remainingSlides += bullet_points
            contents = ''

        
        elif contents.startswith('```mermaid'):
            # print("###diagram-slide###")
            diagram = normal_slide.format(slide_title=slide_title, content=contents, image_side=slide_side[get_random_value()], image_url=image_url, hr_line=hr_line, page_no=page_no)
            # print(diagram)
            remainingSlides += diagram

        elif contents.startswith('```'):
            # print("###code-slide###")
            code = normal_slide.format(slide_title=slide_title, content=contents, image_side=slide_side[get_random_value()], image_url=image_url, hr_line=hr_line, page_no=page_no)
            # print(code)
            remainingSlides += code
            contents = ''
        
        elif contents[0].isalpha():
            # print("###normal-slide###")
            data = normal_slide.format(slide_title=slide_title, content=contents, image_side=slide_side[get_random_value()], image_url=image_url, hr_line=hr_line, page_no=page_no)
            # print(data)
            remainingSlides += data
            contents = ''

        elif contents.startswith(''):
            print("ok! that's the error")
        else:
            print("Cant find the slide type")

        contents = ''

f.close()

f2 = open('ai-generated.md', 'w')
f2.writelines(slideStructure)
f2.writelines(titleSlide)
f2.writelines(toc)
f2.writelines(introductionSlide)
# f2.writelines(bullet_points_slide)
# f2.writelines(normal_slide)
f2.writelines(remainingSlides)
# f2.writelines(generate_toc())
f2.close()
# generate_toc()

# f3 = open('remaining.md', 'w')
# f3.writelines(remainingSlides)

# TODO
# Include dynamic images related to the topic
# remove : form title if any available
# include introduction slide dynamically
# include thank you slide 
# add v-click to the content(normal-slide) (animation)
# include two paragraph containers and prompt for two different paragraphs