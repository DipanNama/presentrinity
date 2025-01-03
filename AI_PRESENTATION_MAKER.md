```mermaid
---
title: AI Presentation maker 

---

flowchart TD;
    python
    slidev
    python --(1)--> flask --(2) service/3000--> nextjs --(3) ask prompt for ppt--> chatGPT --(5) ask for extra info to put--> loading --(6) sends extra data for proper output--> python
    loading --(7) shifts to --> presentation
    python -- (9) run system command --> system --(10) npx slidev template.md--> slidev --(12) creates new service/3030--> presentation --(13) download ppt --> python
    chatGPT -- (4) generates data--> python --(8) final data got form all sources--> template
    template --(11) gets final data for ppt generation--> slidev
    system --(14) npx slidev export template.md (format)--> slidev
```

# Template features

- already predefined template
- give the same template to chatGPT and ask for generating blank places defined with []
- AI image generation
- 2 column architecture
- minimilast
- predefined background image
- user details like name, id, and other data will be there (parsed using chatGPT by asking why and for whom is data for)
- every section will have atmost 4-5 points and atleast 2 points
- heading line will be generated separetely
- page nos are there
- current date will be there
- home page background image
- hannk you page
- conclusion page
- on every point there will be a `v-click` class
- code line animation highlight with other lines fade out
- image in every section right side or down side
- contents page will be there
- introduction
