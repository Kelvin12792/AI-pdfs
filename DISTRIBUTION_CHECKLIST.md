# DISTRIBUTION_CHECKLIST.md — Pre-Upload Checklist

## How to Use This File

Run through this checklist completely before uploading any edition to any platform. Check every box. Do not upload if any box is unchecked. Sign off with date and edition number at the bottom of each platform section.

---

## Universal Pre-Upload Checks (All Platforms)

Run these before proceeding to any platform-specific checklist.

- [ ] PDF file opens without errors on a smartphone (Android and/or iPhone)
- [ ] PDF file opens without errors on a laptop (Mac and/or Windows)
- [ ] All fonts are embedded — verify with Adobe Acrobat or `pypdf` metadata check
- [ ] All images render correctly — no broken image placeholders
- [ ] Cover art is crisp — no pixelation at full A4 size
- [ ] All body diagrams are crisp — readable at half-page width
- [ ] File size is under 10MB
- [ ] No placeholder text remains (no `[DIAGRAM: ...]`, no `[TBD]`, no `[INSERT]`)
- [ ] All CTAs contain correct, active links or social handles
- [ ] Edition number and title on cover matches EDITION_REGISTRY.md
- [ ] Author line reads exactly: "by Kelvin M — AI Educator & Researcher"
- [ ] Glossary contains every technical term used in the body
- [ ] Quiz contains exactly 10 questions in correct format mix
- [ ] Answer key is saved in `structured/edition_{NN}_{slug}/answer_key.md` — NOT in the PDF
- [ ] Reflection question matches correct rotation for this edition number
- [ ] Next edition teaser is present and ends on a cliffhanger
- [ ] All six CTAs are present in correct order
- [ ] Edition registered in EDITION_REGISTRY.md
- [ ] Build logged in CHANGELOG.md

---

## Platform 1 — Selar

**URL:** https://selar.co  
**File format accepted:** PDF  
**Maximum file size:** 500MB (PDF well within limit)  
**Cover image required:** Yes — separate upload, not embedded in PDF

### Selar Pre-Upload Checklist

**File:**
- [ ] PDF exported as `edition_{NN}_{slug}_v{version}.pdf`
- [ ] File size confirmed under 10MB
- [ ] File tested — opens cleanly on mobile browser

**Cover Image for Selar Listing:**
- [ ] Cover image exported as JPG, 1200 × 1680px (72 DPI — web display)
- [ ] Cover image saved as `assets/covers/edition_{NN}_cover_selar.jpg`
- [ ] Cover image file size under 2MB

**Listing Metadata:**
- [ ] Product title: `[Series Name] — Edition {NN}: {Title}`
- [ ] Short description (max 160 characters): Written and proofread
- [ ] Long description: Includes what the reader will learn, who it's for, and what's inside
- [ ] Category selected: Education / E-Book
- [ ] Price set (or marked free): Confirmed per access model decision
- [ ] Tags added: ai, artificial intelligence, beginner, education, kelvin m

**Post-Upload:**
- [ ] Preview link tested — PDF loads and displays correctly
- [ ] Payment flow tested (if paid)
- [ ] Product URL saved in EDITION_REGISTRY.md

**Sign-off:** Edition ____ uploaded to Selar on ____________ by Kelvin M

---

## Platform 2 — Gumroad

**URL:** https://gumroad.com  
**File format accepted:** PDF  
**Maximum file size:** 250MB (PDF well within limit)  
**Cover image required:** Yes — separate upload

### Gumroad Pre-Upload Checklist

**File:**
- [ ] PDF exported as `edition_{NN}_{slug}_v{version}.pdf`
- [ ] File size confirmed under 10MB

**Cover Image for Gumroad Listing:**
- [ ] Cover image exported as PNG or JPG, minimum 1280 × 720px (landscape) OR 960 × 1280px (portrait)
- [ ] Gumroad recommends portrait — use 960 × 1280px crop from cover art
- [ ] Saved as `assets/covers/edition_{NN}_cover_gumroad.jpg`
- [ ] File size under 5MB

**Listing Metadata:**
- [ ] Product name: `[Series Name] — Edition {NN}: {Title}`
- [ ] Description: Full description with learning objectives, who it's for, what's inside, and CTA
- [ ] Price set (or pay-what-you-want / free): Confirmed per access model decision
- [ ] Category: eBook / Education
- [ ] Tags: ai education, artificial intelligence, beginner guide, kelvin m
- [ ] "Call to action" button text set to: "Get it now"

**Gumroad-Specific Settings:**
- [ ] "Ratings" enabled
- [ ] "Reviews" enabled
- [ ] Thank you email customised with: next edition teaser + social media links for Kelvin M

**Post-Upload:**
- [ ] Preview page reviewed — all content displays correctly
- [ ] Test purchase completed (free copy)
- [ ] Download link tested — PDF downloads and opens correctly
- [ ] Product URL saved in EDITION_REGISTRY.md

**Sign-off:** Edition ____ uploaded to Gumroad on ____________ by Kelvin M

---

## Platform 3 — KDP (Kindle Direct Publishing)

**URL:** https://kdp.amazon.com  
**Format for eBook:** PDF or reflowable EPUB (PDF recommended for this design-heavy series)  
**Format for print:** PDF with KDP print specifications  
**Note:** KDP is suitable for print-on-demand physical copies — the digital PDF sales should go through Selar/Gumroad primarily

### KDP Pre-Upload Checklist (Print Edition)

**Interior File (the PDF):**
- [ ] PDF is Portrait A4 — 210mm × 297mm
- [ ] All fonts embedded
- [ ] Images at minimum 300 DPI
- [ ] No crop marks or bleed added (KDP adds its own)
- [ ] Interior PDF saved as `edition_{NN}_{slug}_KDP_interior_v{version}.pdf`

**Cover File (separate KDP cover):**
- [ ] KDP cover built using KDP Cover Calculator for correct dimensions
- [ ] Cover includes front, spine, and back (for print)
- [ ] Front of KDP cover matches series design exactly
- [ ] Spine includes: series name, edition title, "Kelvin M"
- [ ] Back includes: short description, author name, barcode area (leave blank — KDP adds)
- [ ] KDP cover saved as `assets/covers/edition_{NN}_cover_KDP.pdf`

**KDP Listing Metadata:**
- [ ] Book title: `[Series Name] — Edition {NN}: {Title}`
- [ ] Author name: Kelvin M
- [ ] Description: Same as Gumroad description, reformatted for Amazon style
- [ ] Keywords (7 maximum): artificial intelligence, AI for beginners, machine learning basics, AI education, learn AI, technology education, Kelvin M
- [ ] Categories: selected 2 BISAC categories (e.g. Computers > Artificial Intelligence, Education > Study Skills)
- [ ] Language: English
- [ ] Publication date: Set to release date
- [ ] Price: Set per access model decision

**Post-Upload:**
- [ ] KDP previewer used — interior and cover reviewed
- [ ] Print proof ordered before first public sale (physical editions only)
- [ ] ASIN saved in EDITION_REGISTRY.md

**Sign-off:** Edition ____ uploaded to KDP on ____________ by Kelvin M

---

## Social Media Distribution Checklist

Run this checklist when announcing a new edition on each platform.

### WhatsApp Groups & Telegram Channel
- [ ] PDF shared directly as file attachment (not link)
- [ ] Announcement message written: 2–3 sentences + download link
- [ ] Cover image included in announcement message

### LinkedIn
- [ ] Post written: hook sentence + 3 key takeaways from the edition + download link
- [ ] Cover image attached as post image
- [ ] Relevant hashtags added: #AIEducation #ArtificialIntelligence #LearnAI #KelvinM

### Twitter / X
- [ ] Thread created: hook tweet + 3–5 key insight tweets + final tweet with download link
- [ ] Cover image attached to first tweet
- [ ] Relevant hashtags: #AI #ArtificialIntelligence #LearnAI

### Instagram
- [ ] Cover image posted as feed post
- [ ] Caption: hook sentence + "Link in bio" + relevant hashtags
- [ ] Story posted with swipe-up link (or link sticker)

### Email Newsletter
- [ ] Newsletter draft written: subject line, preview text, body (hook + 3 takeaways + download CTA)
- [ ] Subject line A/B tested if possible
- [ ] Send time scheduled for optimal engagement (Tuesday–Thursday, 8–10am recipient timezone)
