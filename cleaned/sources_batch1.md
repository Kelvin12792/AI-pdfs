# Fact-Check Report: Batch 1
# Date: 2026-03-16
# Reviewer: Claude (automated first pass — requires human verification)

---

## Verification Results

### VERIFIED ✓

1. **Claude Code reached $1B annualized revenue** (Post 11)
   Anthropic officially confirmed Claude Code hit $1 billion in annualized run-rate revenue by November 2025, just six months after public launch. By February 2026 it reached $2.5B annualized. Source: Anthropic official announcement and multiple credible outlets including TechCrunch.

2. **Context window sizes: Claude 200K, GPT-5 400K, Gemini 1M tokens** (Post 11)
   As of early 2026, these figures are accurate for current flagship models. Claude Opus 4.5 has a 200K standard context window (with a 1M beta available via API). GPT-5.2 supports 400K tokens. Gemini 3 Pro supports 1 million tokens. NOTE: These numbers change with model updates; always cite the specific model version and date.

3. **TikTok slideshows (carousels) get 2.9x more comments than video** (Post 17, referenced indirectly)
   TikTok's own data confirms carousels get 1.9x more likes, 2.9x more comments, and 2.6x more shares than video. An independent study by Fanpage Karma found 81% higher overall engagement rates for carousels. The 2.9x figure specifically applies to comments, not overall engagement. Source: TikTok internal data as reported by PostEverywhere.ai (Feb 2026).

4. **Claude Code can be run with local models via Ollama for free** (Post 7)
   Technically accurate with important caveats. Since Ollama v0.14.0 (January 2026), Ollama exposes an Anthropic-compatible Messages API, allowing Claude Code's CLI and tooling to work with local open-source models. However, the underlying AI model is NOT Claude — it is a different, smaller open-source model (e.g., Qwen, GPT-OSS). The cleaned file correctly flagged this distinction.

5. **AI-generated citations have high fabrication rates** (Post 11)
   The claim "nearly half of AI-generated citations are fabricated" is in the right ballpark but imprecise. Actual rates vary significantly by model and task: GPT-3.5 fabricated ~55% of citations; GPT-4/4o fabricated 18-28.6% depending on the study and topic. A Tow Center/Columbia study found over 60% of AI search engine citations contained errors or were fabricated. The cleaned file's phrasing of "nearly half" is a reasonable general approximation but should not be cited as a precise figure.

---

### UNVERIFIED ⚠️

1. **Revenue of over $10,000/month from AI content creation pipeline** (Post 21)
   Self-reported income claim with no independent verification. While some AI content creators do earn at this level (a Fortune article documented one creator earning $60K/month across multiple channels), this is the exception, not the norm. YouTube Shorts pay $0.01-$0.07 per 1,000 views; reaching $10K/month from ad revenue alone requires hundreds of millions of monthly views. Most creators earn far less. DO NOT present as typical or expected.

2. **365 videos in 2-3 months using an AI pipeline** (Post 21)
   Plausible for very simple, templated content (e.g., slideshows with AI voiceover over public domain images), but depends heavily on content type and quality standards. No independent verification found. The claim is more of an estimate than a proven benchmark.

3. **Content platform payout model specifics** (Post 21)
   Platform payout rates change frequently and vary by region, niche, and engagement. No specific verification possible without knowing the exact platform referenced. YouTube Shorts RPM ranges from $0.01-$0.07 per 1,000 views; TikTok Creator Program pays roughly $1 CPM on videos over 60 seconds.

4. **54-year-old consultant built 6 AI agents in 3 weeks with zero coding experience** (Post 24)
   Anecdotal claim that cannot be independently verified. The timeline is aggressive but not impossible using no-code/low-code agent platforms (e.g., Flowise, n8n, Make.com). However, without identifying details, this cannot be confirmed. Treat as an illustrative story, not a verified case study.

5. **$588 MRR from AI-generated social media content** (Post 17)
   Unverifiable personal income claim. While technically possible through affiliate links, digital products, or services promoted via AI-generated content, this specific figure cannot be confirmed. DO NOT present as typical or expected.

6. **500K+ views in 5 days on social media** (Post 17)
   Unverifiable without platform data access. Viral content can absolutely reach these numbers, but presenting it as a replicable result would be misleading. Treat as anecdotal.

7. **$0.50 per AI-generated social media post** (Post 17)
   Plausible given current API pricing for text generation and image generation, but varies significantly based on model choice, image resolution, and post complexity. A simple text post with one AI-generated image could cost roughly this amount using budget APIs, but more complex content would cost more.

8. **~$8/month fixed cost for self-hosted AI agent system** (Post 15)
   Unlikely for a production-quality system. Research shows even minimal self-hosted setups cost $50+/month, with most realistic deployments costing $1,000-$5,000/month. The $8 figure may refer only to server hosting costs (e.g., a low-tier VPS), excluding the LLM API costs that dominate real-world expenses. Misleading without full context.

9. **Agent coordination, memory persistence, and personality evolution capabilities** (Post 15)
   Technically possible with current frameworks (LangGraph, CrewAI, custom implementations), but the sophistication described represents a custom, developer-built implementation, not an out-of-the-box product. The gap between "technically possible" and "reliably available" is significant.

10. **AI agents can reliably handle complex autonomous tasks across multiple languages** (Post 22)
    Current agent reliability varies significantly. While AI agents can perform many autonomous tasks, reliability drops sharply with task complexity. Multi-language support exists but accuracy varies by language. Present with nuance rather than as a solved problem.

11. **94 code commits in a single day from AI agents** (Post 23)
    While technically possible with automated systems, a Dev.to post documenting a similar experience (94 commits over 27 days) explicitly warned that high commit counts create "a false sense of progress." Research shows AI-assisted teams produce 98% more pull requests but PR review time balloons by ~91%. Volume does not equal quality.

12. **7 pull requests in 30 minutes from AI agents** (Post 23)
    Plausible with automation, but meaningless without context about complexity and quality. As noted above, AI-assisted commits are merged 4x faster than regular commits, raising security concerns and quality issues.

13. **AI spreadsheet tools can "read every tab, formula, and dependency"** (Post 25)
    Marketing claims often exceed real-world reliability. While AI-powered spreadsheet tools are improving rapidly, performance varies by spreadsheet complexity and tool. Present as a developing capability, not a guaranteed feature.

14. **Pricing for AI-powered spreadsheet tools** (Post 25)
    Pricing changes frequently. Any specific figures should be verified at time of publication.

15. **Security vulnerability in AI-spreadsheet integrations** (Post 25)
    Not verified in this search. If referenced in the series, verify current status and whether it has been patched.

16. **"You don't need advanced maths or coding to master AI agents"** (Post 26)
    Partially true. Understanding AI agent concepts requires no technical skills. But building production-grade agents currently does require programming knowledge. Using no-code agent platforms is accessible to non-technical users, but capabilities are more limited. The distinction between understanding, using, and building matters here.

17. **Company valuations and AI model capabilities referenced** (Post 27)
    Too vague to verify without specific numbers. Any specific valuation or capability claims should be independently checked before inclusion.

18. **Real estate AI follow-up system "that would have cost $15,000 from an agency"** (Post 29)
    The $15,000 figure is plausible for a custom-built solution from a development agency. AI consulting project fees range from $10,000-$500,000+. However, off-the-shelf AI follow-up tools for real estate cost $49-$166/month. The comparison is potentially misleading — it compares a custom build to commodity SaaS pricing.

19. **System described as "11 modules, 80+ files"** (Post 20)
    This describes a specific personal implementation. Cannot verify the exact scope but the description is plausible for a developer-built AI system. The cleaned file correctly flags that this should NOT be presented as necessary or recommended for beginners.

---

### FALSE ✗

1. **"Running Claude for free locally"** (Post 7 — partially false)
   The framing is misleading. What runs locally is NOT Claude. It is a different, open-source model (e.g., Qwen 3.5, GPT-OSS) accessed through Claude Code's CLI interface via Ollama's Anthropic-compatible API. The Claude Code agent tooling runs locally, but the AI model intelligence is a substitute, not the real thing. A 4B-parameter local model will not match Claude Opus 4.6 for complex reasoning. The cleaned file correctly identified this distinction. For the series: this is a useful teaching moment about understanding what software you are actually running.

---

### OPINION (Not Fact)

1. **"90% of releases are benchmark releases dressed up as business releases"** (Post 10)
   This is a personal estimate and opinion, not a verified statistic. The underlying sentiment — that most AI releases are incremental rather than revolutionary — is broadly supported by industry observation, but the specific "90%" figure is fabricated as a rhetorical device. DO NOT cite as a statistic. If used in the series, frame as: "Many industry observers note that most AI releases are small improvements, not game-changing breakthroughs."

2. **Revenue projections for AI services ($2K-$12K/month)** (Post 29)
   These are estimates and projections, not verified income data. Income from AI services varies enormously based on skill, market, effort, and niche. AI consulting rates range from $100-$500/hour and project fees from $10K-$500K+, so significant income is possible, but specific monthly projections should be presented as potential ranges, not guarantees.

3. **Revenue claims from Post 12 ($3M total, $31,373/month, $300K from a specific venture)**
   These appear to be unverified testimonials from a sales page. Self-reported income claims in online marketing contexts are notoriously unreliable. DO NOT include in educational content.

4. **"AI makes the wrong humans irrelevant"** (Post 27)
   This is a perspective and opinion, not a factual claim. Present as one viewpoint in a broader discussion about AI and human skills, not as an established truth.

5. **The internet/1995 analogy for AI adoption** (Post 16)
   A common and historically reasonable framing, but the direct comparison should be presented as a perspective, not a proven parallel. Different technologies follow different adoption curves, and the AI trajectory is not guaranteed to mirror the internet's path.

6. **"These are ideas nobody is building yet"** (Post 9)
   Unverifiable and almost certainly false. Many of the AI service categories described (AI setup for businesses, team training, automated workflows) already have active competitors. The opportunity is real; the claim of no competition is not.

7. **$75K consulting packages for AI implementation** (referenced in revenue claims)
   While $75K falls within the documented range for mid-tier AI consulting projects ($10K-$500K+), presenting it as a standard or achievable price point without context about the expertise and value required would be misleading. Frame as aspirational, not typical.

---

## Detailed Analysis

### Item 1: Nav Toor — "Running Claude Code for FREE locally"
- **Original claim:** Claude Code can be run for free with no rate limits locally on your computer
- **Source post:** Post 7
- **Verification status:** PARTIALLY FALSE / MISLEADING
- **Evidence:** Since January 2026, Ollama (v0.14.0+) provides an Anthropic-compatible Messages API that allows Claude Code's CLI tooling to interface with local open-source models. This is real and functional. However, the AI model running locally is NOT Claude — it is a substitute (Qwen, GPT-OSS, etc.) with significantly less capability. Performance is also hardware-dependent; on an M1 Max with 64GB RAM, even simple tasks took 55 seconds to 2+ minutes.
- **Sources:** Towards Data Science, Ollama Blog, multiple technical walkthroughs
- **Recommendation:** USE WITH CORRECTION. This is a valuable teaching moment about the difference between an AI tool's interface and the AI model's intelligence. The concept of "local AI vs. cloud AI" is useful for the series. Always clarify that running Claude Code with a local model means using a different, less powerful AI.

### Item 2: "Nearly half of AI-generated citations are fabricated"
- **Original claim:** Nearly half of AI-generated citations are fabricated
- **Source post:** Post 11 (Machina's 30-day roadmap)
- **Verification status:** VERIFIED WITH NUANCE
- **Evidence:** Multiple peer-reviewed studies confirm high fabrication rates: GPT-3.5 fabricated ~55% of citations (Scientific Reports study); GPT-4o fabricated ~20% (JMIR Mental Health, Nov 2025); Tow Center found >60% of AI search engine citations had errors or were fabricated (March 2025). Rates vary significantly by model, topic, and study methodology.
- **Sources:** Nature Scientific Reports, JMIR Mental Health, Tow Center/Columbia University, Nieman Journalism Lab
- **Recommendation:** USE WITH PRECISION. Instead of "nearly half," write something like: "Studies have found that anywhere from 20% to over 50% of citations generated by AI are fabricated or contain significant errors, depending on the AI model and the subject matter." This is a critically important concept for the series and should be included in editions about AI limitations and reliability.

### Item 3: "84% of the world has never used AI"
- **Original claim:** 84% of the world has never used AI
- **Source post:** Post 29 (Corey Ganim)
- **Verification status:** UNVERIFIED — originated from viral social media, not formal research
- **Evidence:** This statistic comes from a viral visualization by Damian Player posted on X/LinkedIn in February 2025. It appears to be a back-of-the-envelope estimate, not a rigorous study. No peer-reviewed source or formal market research has been identified. However, the directional claim is partially supported: Eurostat found only 32.7% of EU citizens aged 16-74 used generative AI in 2025; US Census data shows only 18.2% of American companies use AI.
- **Sources:** Damian Player (X/LinkedIn), Eurostat, US Census Bureau
- **Recommendation:** DO NOT USE the specific "84%" figure. Instead, if making this point, write: "Research suggests that the vast majority of the world's population has never directly used an AI tool" and cite the Eurostat or similar institutional data. The general point is powerful and directionally accurate; the specific number is not reliably sourced.

### Item 4: Claude Code "$1B annualized revenue"
- **Original claim:** Claude Code reached $1 billion in annualized revenue
- **Source post:** Post 11
- **Verification status:** VERIFIED
- **Evidence:** Anthropic officially announced this milestone. Claude Code launched publicly in May 2025 and reached $1B in annualized run-rate revenue by November 2025. By February 2026, it reached $2.5B annualized. For comparison, ChatGPT took ~11 months to reach a similar milestone.
- **Sources:** Anthropic official announcement, TechCrunch, Yahoo Finance
- **Recommendation:** SAFE TO USE. This is a well-documented milestone from official company disclosures. If citing, note the date (November 2025) and specify "annualized run-rate revenue" rather than just "revenue." This figure illustrates the rapid growth of AI tools and can be used in editions about the AI industry landscape.

### Item 5: Context window sizes
- **Original claim:** Claude has 200K tokens, GPT-5 has 400K tokens, Gemini has 1M tokens
- **Source post:** Post 11
- **Verification status:** VERIFIED (as of early 2026)
- **Evidence:** Claude Opus 4.5: 200K standard (1M beta via API). GPT-5.2: 400K tokens. Gemini 3 Pro: 1M tokens. These are confirmed by official documentation and multiple independent comparisons.
- **Sources:** IntuitionLabs comparison, multiple AI model comparison articles
- **Recommendation:** USE WITH DATE STAMP. These numbers are accurate as of March 2026 but change with model updates. If included in the series, always note: "As of [date], these are the current context window sizes. Check for updates, as these numbers change frequently." The concept of context windows is more important for the series than specific numbers.

### Item 6: "90% of releases are benchmark releases"
- **Original claim:** 90% of AI releases are benchmark releases dressed up as business releases
- **Source post:** Post 10
- **Verification status:** OPINION (Not Fact)
- **Evidence:** No data source exists for this claim. It is a rhetorical estimate expressing the opinion that most AI releases are incremental. The underlying sentiment has broad industry support but the specific percentage is invented.
- **Recommendation:** DO NOT cite as a statistic. If the concept is useful for the series, rephrase as: "Many AI industry watchers observe that most new AI releases are small, incremental improvements rather than major breakthroughs — even when the marketing makes them sound revolutionary."

### Item 7: TikTok slideshows engagement
- **Original claim:** TikTok slideshows get 2.9x more comments
- **Source post:** Post 17 (referenced in Part 2)
- **Verification status:** VERIFIED
- **Evidence:** TikTok's own internal data confirms carousels receive 2.9x more comments, 1.9x more likes, and 2.6x more shares compared to video content. Independently, Fanpage Karma found 81% higher overall engagement for carousels.
- **Sources:** TikTok internal data (as reported by PostEverywhere.ai), Fanpage Karma study
- **Recommendation:** SAFE TO USE with attribution to TikTok's internal data. Note that this specifically applies to comments, not all engagement metrics. Also note that Fanpage Karma found shares were about a third lower for carousels compared to video, so the advantage is engagement-specific.

### Item 8: Revenue claims from Post 9 (AI business ideas)
- **Original claim:** Various revenue projections for AI services
- **Source post:** Post 9
- **Verification status:** OPINION (Not Fact)
- **Evidence:** Revenue projections from social media posts about AI services are estimates, not verified income. AI consulting rates ($100-$500/hr) and project fees ($10K-$500K+) are documented, confirming that significant income is possible, but individual claims are unverifiable.
- **Recommendation:** DO NOT reproduce specific dollar figures as facts. The concept that AI creates business opportunities is sound; specific income claims are not.

### Item 9: Revenue claims from Post 12
- **Original claim:** $3M total, $31,373/month, $300K from a specific venture
- **Source post:** Post 12
- **Verification status:** OPINION (Not Fact) / UNVERIFIABLE
- **Evidence:** These are self-reported testimonials from what appears to be a sales page. No independent verification is possible.
- **Recommendation:** DO NOT include in educational content. These claims are from promotional material and should be completely excluded from the series.

### Item 10: Post 21 revenue and production claims
- **Original claim:** $10,000+/month from AI content creation; 365 videos in 2-3 months
- **Source post:** Post 21
- **Verification status:** UNVERIFIED
- **Evidence:** While some AI creators earn at this level, it represents the top tier, not the typical outcome. YouTube Shorts RPM ($0.01-$0.07/1,000 views) means $10K/month from ad revenue alone requires hundreds of millions of monthly views. The 365-video claim is plausible for simple content but unverified.
- **Recommendation:** DO NOT present as typical or expected outcomes. If discussing AI content creation income, frame as: "Some creators have built significant income streams using AI tools, but results vary enormously based on niche, quality, consistency, and audience building."

### Item 11: Post 22 — AI agent promotional claims
- **Original claim:** Specific AI agent platform can reliably handle complex autonomous tasks
- **Source post:** Post 22
- **Verification status:** UNVERIFIED
- **Evidence:** The post is partly promotional. Current AI agent capabilities are real but reliability varies significantly with task complexity.
- **Recommendation:** USE THE CONCEPT, NOT THE PRODUCT CLAIMS. The chatbot-vs-agent distinction is valuable educational content. The specific product capabilities should not be cited.

### Item 12: Post 23 — Commit and PR volume claims
- **Original claim:** 94 code commits in a single day; 7 pull requests in 30 minutes
- **Source post:** Post 23
- **Verification status:** UNVERIFIED / MISLEADING
- **Evidence:** High commit volumes are technically possible with AI coding agents, but research shows volume does not equal quality. AI-assisted teams produce more PRs but review time increases ~91%, and security exposure increases ~40%. A documented "94 commits" experience explicitly warned about false productivity signals.
- **Recommendation:** DO NOT cite raw numbers as evidence of productivity. If discussing AI coding assistance, note that AI can increase output volume but quality review remains essential. The concept of AI teams is valuable; the specific metrics are misleading.

### Item 13: Post 25 — AI spreadsheet capabilities
- **Original claim:** AI can read every tab, formula, and dependency in a spreadsheet
- **Source post:** Post 25
- **Verification status:** UNVERIFIED
- **Evidence:** AI spreadsheet tools are rapidly improving, but marketing claims often exceed real-world reliability. Performance varies by tool and spreadsheet complexity.
- **Recommendation:** Present as a developing capability: "AI tools are increasingly able to analyze spreadsheet structure, trace formula dependencies, and explain complex spreadsheets in plain language." Avoid absolute claims about what AI "can" do with spreadsheets.

### Item 14: Post 26 — "No advanced maths or coding needed to master AI agents"
- **Original claim:** You do not need advanced maths or years of coding to get started with AI agents
- **Source post:** Post 26
- **Verification status:** PARTIALLY TRUE
- **Evidence:** Understanding AI agent concepts requires no technical skills. Using no-code agent builders is accessible to non-technical users. However, building production-grade agents currently does require programming knowledge.
- **Recommendation:** USE WITH NUANCE. Reframe as: "You do not need advanced maths or coding to understand how AI agents work, or to use pre-built agent tools. However, building custom AI agents from scratch currently requires some programming knowledge."

### Item 15: Post 27 — Company valuations and model capabilities
- **Original claim:** Various unspecified claims about company valuations and AI model capabilities
- **Source post:** Post 27
- **Verification status:** UNVERIFIED (too vague to check)
- **Recommendation:** Any specific numbers should be independently verified before inclusion. The conceptual content (ten human traits AI cannot replace) does not require fact-checking as it is opinion-based.

### Item 16: Post 29 — Revenue projections ($2K-$12K/month) and $15K agency comparison
- **Original claim:** AI services can earn $2K-$12K/month; a real estate AI system would cost $15K from an agency
- **Source post:** Post 29
- **Verification status:** OPINION / PLAUSIBLE BUT UNVERIFIED
- **Evidence:** AI consulting project fees range $10K-$500K+, so $15K for a custom system is plausible. Monthly AI service income of $2K-$12K is possible but not guaranteed. Off-the-shelf real estate AI tools cost $49-$166/month, making the $15K comparison potentially misleading.
- **Recommendation:** DO NOT cite specific dollar figures. The concept that AI skills create earning opportunities is supported by market data; specific income projections are speculative.

---

## Summary for Series Use

### Safe to Use (with proper framing)
- Claude Code $1B revenue milestone (verified, cite date)
- Context window sizes (verified, always include date stamp)
- TikTok carousel engagement statistics (verified, specify "comments" not "overall")
- AI citation fabrication rates (verified, use range not single number)
- Cloud vs. local AI distinction (verified concept, correct the misleading framing)

### Use Concept Only (remove specific numbers)
- AI creates new business opportunities (remove revenue projections)
- AI content creation at scale (remove income claims)
- AI agent capabilities (remove product-specific claims)
- AI coding productivity (remove commit/PR volume claims)

### Do Not Use
- "84% of the world has never used AI" (no reliable primary source)
- "90% of releases are benchmark releases" (invented statistic)
- Any self-reported revenue figures from social media posts
- Any claims presented as facts that are actually opinions or estimates

### Requires Date-Stamping
- All context window sizes
- All pricing information
- All platform payout rates
- All model capability comparisons

---

*This report is an automated first pass. All items marked VERIFIED should still be confirmed by a human reviewer before publication. All sources should be independently checked. Statistics and claims can become outdated rapidly in the AI industry — re-verify any data point that is more than 3 months old at time of publication.*
