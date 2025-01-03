---
title: Presentation Template
theme: dracula
layout: center
favicon: https://upload.wikimedia.org/wikipedia/commons/1/1f/Artificial_Intelligence.svg
background: https://cover.sli.dev
# class: text-white
transition: slide-left

---

<!-- Title Slide -->
<!-- <div style="text-align: center;"> -->
# Presentation Title
### Subtitle or Topic Explanation
#### Your Name | ID: YourID | Designation
<!-- _Date: {{new Date().toLocaleDateString()}}_ -->
<!-- </div> -->

<div class="h-full w-full" style="background-image: url('https://source.unsplash.com/featured/?technology,abstract'); background-size: cover; background-position: center;"></div>

---

## Table of Contents

1. **Introduction**
2. **Main Content Section 1**
3. **Main Content Section 2**
4. **Conclusion**
5. **Thank You**

---

<!-- Introduction Section -->
## Introduction

<Arrow v-bind="{ x1:10, y1:10, x2:200, y2:200 }" />
<div class="grid grid-cols-2 gap-6">
<div>

- **Who is this for?**  
  Developers, students, or professionals. <span class="v-click"/>

- **Why this topic?**  
  Addressing real-world challenges or sharing research insights. <span class="v-click"/>

- **Overview**  
  Brief description of the subject matter. <span class="v-click"/>

</div>
<div>
<img src="https://source.unsplash.com/featured/?team,discussion" alt="Introduction Image" class="rounded shadow" />
</div>
</div>

---

<!-- Main Content Section 1 -->
## [Section Title]

<div class="grid grid-cols-2 gap-6">
<div>
<img src="https://source.unsplash.com/featured/?technology,innovation" alt="Section 1 Image" class="rounded shadow" />
</div>
</div>

<v-clicks depth="2">

- Item 1
  - Item 1.1
  - Item 1.2
- Item 2
  - Item 2.1
  - Item 2.2

</v-clicks>
<v-click at="+1"><div> visible after some clicks </div></v-click>
<div v-click.hide="'-1'"> hidden after some clicks </div>

```js {none|1|2}{at:'+2'}
1  // highlighted after 7 clicks
2  // highlighted after 8 clicks
```

---

<!-- Main Content Section 2 -->
## [Section Title]

<div class="grid grid-cols-2 gap-6">
<div>

- Key Point 1: Explanation. <span class="v-click"/>
- Key Point 2: Explanation. <span class="v-click"/>
- Key Point 3: Explanation. <span class="v-click"/>
- Key Point 4: Explanation. <span class="v-click"/>

</div>
<div>
<img src="https://source.unsplash.com/featured/?ai,robots" alt="Section 2 Image" class="rounded shadow" />
</div>
</div>

---

<!-- Conclusion Section -->
## Conclusion

<div class="grid grid-cols-2 gap-6">
<div>

- Summary of Key Points: <span class="v-click"/>
- Final Thoughts or Recommendations: <span class="v-click"/>
- Acknowledgments (if applicable): <span class="v-click"/>

</div>
<div>
<img src="https://source.unsplash.com/featured/?summary,conclusion" alt="Conclusion Image" class="rounded shadow" />
</div>
</div>

---

<!-- Thank You Slide -->
# Thank You!
### Questions?
#### Your Contact Details  
_Email: your.email@example.com | Website: yourwebsite.com_

<div class="h-full w-full" style="background-image: url('https://source.unsplash.com/featured/?thankyou,abstract'); background-size: cover; background-position: center;"></div>

---

<img
  v-click
  class="absolute -bottom-9 -left-7 w-80 opacity-50"
  src="https://sli.dev/assets/arrow-bottom-left.svg"
  alt=""
/>

---