# Nand Kishor Vishwakarma | 3D AI/ML Portfolio

B.Tech CSE (AI), Babu Banarasi Das University, Lucknow.
Yeh project Python se ek static portfolio website (`public/index.html`) banata hai. Koi package install nahi karna.

## Folder structure

```
portfolio-project/
  data.py                      <- SIRF ISE EDIT KARO (naam, skills, projects, links)
  build.py                     <- website banata hai (python build.py)
  templates/index.template.html<- design + 3D animation (edit zaroori nahi)
  assets/                      <- photo.jpg aur resume.pdf yahan rakho
  public/                      <- ready website (yahi deploy hoti hai)
  vercel.json, render.yaml     <- deploy settings
```

## 1. Local pe chalana

1. Python 3.8+ install karo (python.org, "Add Python to PATH" tick karo). Check: `python --version`
2. Terminal mein folder kholo: `cd portfolio-project`
3. `data.py` kholo (VS Code/Notepad) aur `[brackets]` wali jagah apni real details bharo.
4. Photo `assets/photo.jpg` aur resume `assets/resume.pdf` naam se rakho.
5. Run: `python build.py --serve`
6. Browser mein kholo: http://localhost:8000 (band karne ke liye Ctrl+C)

Badlav ke baad dobara `python build.py` chalao aur browser mein `Ctrl + Shift + R` karo.

## 2. GitHub pe upload

Option A (bina git ke): github.com par New repository banao (Public), phir Add file > Upload files, poora folder ka content drag-drop karo (`public/` folder bhi), Commit.

Option B (git se):
```
git init
git add .
git commit -m "My portfolio"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/portfolio.git
git push -u origin main
```
Har update ke baad `python build.py`, phir `git add .`, `git commit -m "update"`, `git push`.

## 3. Vercel pe deploy

1. vercel.com par GitHub se login karo.
2. Add New > Project > apna repo Import karo.
3. Framework Preset: **Other**. Build Command khali. Output Directory: **public** (vercel.json mein pehle se hai).
4. Deploy dabao. 1 minute mein `yourproject.vercel.app` link milega.
5. Aage se `git push` karoge to site khud update hogi.

## 4. Render pe deploy

1. render.com par GitHub se login karo.
2. New > **Static Site** > apna repo select karo.
3. Build Command: `python build.py`. Publish Directory: **public**.
4. Create Static Site. Kuch minute mein `yourproject.onrender.com` link milega.
(`render.yaml` se Blueprint option bhi use kar sakte ho.)

## 5. GitHub Pages (bonus)

Settings > Pages > Deploy from a branch > `main` > folder `/ (root)`. Site root pe `index.html` chahiye, to `public/index.html` ko repo ke root mein bhi copy kar do, ya Vercel/Render use karo.

## Common errors

- `SyntaxError` in data.py: quote ya comma chhoot gaya, error ki line dekho.
- Photo nahi dikh rahi: file ka naam `assets/photo.jpg` hona chahiye, aur `python build.py` dobara chalao.
- Site online purani dikh rahi hai: `public/` folder commit/push hua ya nahi check karo.
- Instagram/LinkedIn link: `data.py` ke `links` mein `yourusername` badlo.
