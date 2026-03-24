# Chapter 9: How to Talk to AI -- The Art of Prompting

---

## Opening

In Chapter 8, you had your first AI conversation. You learned to type full sentences instead of keywords, to give AI a role, to ask follow-up questions, and to refine responses when they were not quite right. Those basics will carry you a long way.

But there is a difference between being able to drive a car and being a good driver. A good driver reads the road ahead, anticipates what is coming, and makes small adjustments that produce a smoother, faster, safer journey. The car is the same. The difference is in how you use it.

This chapter is about becoming a better driver.

The skill of communicating effectively with AI has a name: prompt engineering. The name sounds technical, but the practice is not. Prompt engineering is simply the art of asking AI for what you want in a way that consistently gets you useful results. It is a communication skill, not a coding skill. If you can write a clear email, explain a task to a new employee, or give directions to someone who has never been to your house, you already have the foundation.

What separates someone who gets mediocre results from AI and someone who gets remarkable results is rarely intelligence or technical knowledge. It is the quality of their prompts. And that quality comes from understanding a handful of principles that, once you learn them, you will use in every AI interaction for the rest of your life.

---

## The Prompt Formula: Context, Task, Rules

In Chapter 8, we introduced the idea that specific prompts produce better results than vague ones. Now we are going to make that idea concrete with a formula you can use every time.

Every effective prompt has three components:

**Context** -- Who you are and what your situation is.
**Task** -- What you want the AI to do.
**Rules** -- Any constraints, preferences, or format requirements.

Let us see how this works with a real example.

### A Weak Prompt

"Help me write an email."

This prompt has a task (write an email) but no context and no rules. The AI has no idea who you are, who the email is for, what it is about, what tone to use, or how long it should be. It will produce something generic that probably requires significant editing.

### A Strong Prompt

"I am a freelance graphic designer (context). I need to write an email to a client who has not paid an invoice that is three weeks overdue (task). Keep the tone professional but firm. The email should be under 150 words. Do not threaten legal action but make it clear this needs to be resolved promptly (rules)."

This prompt gives the AI everything it needs. The result will be specific, appropriately toned, the right length, and immediately usable with minimal editing.

### Before and After Comparison

Here is the same request written two ways, so you can see the difference the formula makes.

**Without the formula:**
"Write a cover letter for a job."

**With the formula:**
"I am a recent university graduate with a degree in psychology and six months of internship experience at a mental health clinic (context). Write a cover letter for a junior counsellor position at a community health centre (task). Highlight my empathy, my experience with diverse client populations, and my willingness to learn. Keep the tone professional but warm. One page maximum. Do not use cliches like 'passionate about making a difference' (rules)."

The second prompt will produce a cover letter that sounds like it was written by a human who actually applied for this specific job. The first will produce something that could apply to any job, anywhere, by anyone.

### Practice Exercise

Try building your own prompt using the formula. Think of something you actually need help with, then fill in:

- **Context:** Who am I? What is my situation? What do I already know?
- **Task:** What do I want the AI to do? Be specific about the action.
- **Rules:** What format do I want? What tone? What length? What should it include or avoid?

Write it out, type it into your AI tool, and compare the result to what you would have gotten with a vague prompt. The difference is usually dramatic.

---

## The Seven Prompt Techniques

Beyond the basic formula, there are specific techniques that consistently improve AI output. You do not need to memorise all seven. Learn two or three that are useful for what you do, and add the others as you get more comfortable.

### Technique 1: Role Assignment

You practiced this briefly in Chapter 8. Now let us go deeper.

When you tell AI to act as a specific type of person, you are not just adding flavour. You are shaping the entire structure of its response: the vocabulary it uses, the level of detail it provides, the assumptions it makes, and the perspective it brings.

**Without a role:**
"Explain inflation."

**With a role:**
"You are a high school economics teacher who is known for making complex concepts easy to understand. Explain inflation to a class of students who have never studied economics. Use everyday examples they would recognise."

The first prompt produces an accurate but potentially dry explanation. The second produces an explanation that uses grocery store prices, pocket money, and examples from a teenager's daily life. Same topic. Completely different result.

Here are roles that work well for different situations:

- **"You are a patient tutor"** -- for learning and explanations
- **"You are a senior editor at a major newspaper"** -- for writing feedback
- **"You are a career coach with 20 years of experience"** -- for career advice
- **"You are a doctor explaining a diagnosis to a worried patient"** -- for health information in plain language
- **"You are a sceptical reviewer"** -- for getting honest criticism of your work
- **"You are a friendly customer service representative"** -- for drafting polite responses to complaints

The role you assign should match the kind of response you want. A "sceptical reviewer" will point out weaknesses. A "supportive mentor" will encourage you. Both are useful in different situations.

### Technique 2: Show, Do Not Just Tell (Few-Shot Prompting)

Sometimes the fastest way to explain what you want is to show the AI an example. Instead of describing the format, tone, or style you want, you give the AI one, two, or three examples of what a good response looks like, and then ask it to follow the same pattern.

This technique is called few-shot prompting. "Few-shot" simply means you are giving the AI a few examples (shots) to learn from before it produces its own output.

**Without examples:**
"Write product descriptions for my online store."

**With an example:**
"I write product descriptions for my online store. Here is an example of my style:

'The Weekender Tote -- Built for the person who refuses to check a bag. Fourteen inches of waxed canvas, brass hardware, and a shoulder strap that actually stays on your shoulder. Fits a weekend's worth of clothes, a laptop, and your stubborn independence. Available in moss green and midnight navy.'

Now write a description in the same style for a leather wallet that has RFID-blocking technology, six card slots, and a slim profile."

The AI will match the tone (casual, confident), the structure (name, description, features, personality), and even the sentence rhythm of your example. You never had to explain any of those things. The example did the work for you.

This technique is powerful because it bypasses the difficulty of describing style in words. Trying to explain "I want it to sound confident but not arrogant, casual but not sloppy, and a little bit witty" is hard. Showing an example that has those qualities is easy.

**When to use it:**
- When you have a specific style or format you want replicated
- When the task involves creative writing, branding, or voice consistency
- When you find it easier to show what you want than to describe it
- When you need multiple outputs that all feel consistent with each other

### Technique 3: Step-by-Step Thinking (Chain of Thought)

For complex questions, especially those involving reasoning, analysis, or multi-step problems, you can dramatically improve AI output by asking it to think through the problem step by step before giving its answer.

This technique is called chain-of-thought prompting. It works because AI, like humans, produces better answers to difficult questions when it works through the logic rather than jumping straight to a conclusion.

**Without chain of thought:**
"Should I buy or rent a home in my current situation?"

**With chain of thought:**
"I earn 55,000 per year, have 15,000 in savings, live in a city where average rent is 1,200 per month and average home prices are 280,000. I plan to stay in this city for at least five years. Walk me through the financial considerations step by step, then give me your recommendation based on the analysis."

By asking the AI to "walk through step by step," you get a structured analysis instead of a quick opinion. The AI will consider your income-to-price ratio, savings rate, how long you plan to stay, the break-even point for buying versus renting, and other factors, each laid out in a logical sequence.

**When to use it:**
- Math problems or financial calculations
- Decisions with multiple factors to weigh
- Troubleshooting problems
- Any question where the reasoning process matters as much as the answer

**A simple shortcut:** If you do not want to write a detailed prompt, you can often get the same effect by adding "Think through this step by step before giving your answer" to the end of any question.

### Technique 4: Output Formatting

AI can structure its response in almost any format you specify. Most people never ask for a specific format, so they get plain paragraphs by default. But specifying the format makes the output immediately more useful.

Here are formats you can request:

- **"Give me this as a numbered list."**
- **"Present this as a table with columns for [X], [Y], and [Z]."**
- **"Write this as bullet points, no more than one sentence each."**
- **"Structure this with clear headings and subheadings."**
- **"Give me the answer in exactly three sentences."**
- **"Format this as a pros and cons list."**
- **"Write this as a FAQ with five questions and answers."**

**Example:**
"Compare four popular note-taking apps. Present the comparison as a table with columns for: app name, price, best feature, biggest limitation, and who it is best for."

The AI will produce a clean, scannable table instead of five paragraphs of text. Same information. Completely different usability.

You can also combine format instructions with length constraints: "Summarise this article in exactly five bullet points, each no longer than two sentences." This gives you precise control over what you get back.

### Technique 5: The Revision Loop

In Chapter 8, we introduced the idea of refining AI responses. Now let us turn this into a deliberate technique.

The revision loop works like this: instead of trying to get the perfect result in one prompt, you deliberately plan for multiple rounds. Your first prompt gets a draft. Your second prompt improves it. Your third prompt polishes it.

AI rarely gives its best answer on the first try. This is not a flaw. It mirrors how every skilled professional works. Writers produce drafts before final versions. Designers sketch before they render. Architects draw rough plans before detailed blueprints. The first version is never meant to be the final version.

Here is the revision loop in practice:

**Round 1 (Draft):** "Write a short bio for my professional website. I am a freelance photographer who specialises in food and restaurant photography. I have been working for eight years and my clients include three national restaurant chains."

**Round 2 (Critique):** "Now review what you just wrote. What are the weaknesses? What could be stronger? What cliches did you use?"

**Round 3 (Revise):** "Rewrite the bio, fixing all the weaknesses you identified. Make it more confident and less generic. Start with my most impressive achievement, not a generic introduction."

This three-round process (draft, critique, revise) consistently produces better output than any single prompt, no matter how well-crafted. You are using the AI's ability to evaluate its own work, which pushes it past its default patterns.

**The advanced version:** You can extend this to as many rounds as you need. After the revision, you can ask: "What would make this even better?" Then revise again. Each cycle brings the output closer to your standard.

### Technique 6: Constraints and Boundaries

Sometimes the most useful thing you can tell AI is what NOT to do. Constraints narrow the output and prevent the AI from falling into common patterns you do not want.

**Useful constraints:**
- "Do not use jargon or technical terms."
- "Do not start the email with 'I hope this email finds you well.'"
- "Avoid cliches. No 'at the end of the day' or 'it goes without saying.'"
- "Do not give me more than five options."
- "Do not include any information you are not confident about."
- "Use only short sentences. Nothing longer than fifteen words."
- "Do not use exclamation marks."

Constraints are particularly powerful for writing tasks. AI models have patterns they default to: certain opening phrases, certain transitions, certain ways of structuring information. If those defaults do not match your voice or your needs, constraints redirect the AI away from them.

**Example with constraints:**
"Write a LinkedIn post about my new job promotion. Do not use the phrase 'excited to announce.' Do not use emojis. Do not write more than 100 words. Do not use hashtags. Keep the tone humble and genuine, not boastful."

Those five constraints eliminate the most common LinkedIn cliches and force the AI to produce something that actually sounds like a real person wrote it.

### Technique 7: Breaking Complex Tasks into Steps

When you have a large, complex task, do not try to accomplish it in a single prompt. Break it into smaller pieces and tackle them one at a time, using the AI's memory within the conversation to build on each step.

**Instead of this (one giant prompt):**
"Create a complete business plan for a mobile dog grooming service."

**Do this (step by step):**

1. "I want to start a mobile dog grooming service in a mid-sized city. First, help me define my target customer. Who would use this service and why?"

2. "Good. Now help me figure out the startup costs. What equipment, vehicle modifications, and supplies would I need? Estimate the costs."

3. "Now let us think about pricing. Based on the costs you estimated, what should I charge per session to be profitable? Walk me through the math."

4. "Now help me draft a simple marketing plan. How do I find my first ten customers?"

5. "Finally, combine everything we discussed into a one-page business plan summary."

Each step builds on the last. By the time you reach step five, you have a business plan built from a thoughtful, sequential process, not a rushed attempt to generate everything at once. The final summary will be grounded in the specific details you developed together.

This technique also gives you control. After each step, you can redirect, add information, or change direction. If you do not like the target customer analysis, you can refine it before moving on to costs. You are steering the process, not just hoping for a good result.

---

## Before and After: Five Real Prompts Transformed

Here are five common prompts that beginners write, followed by improved versions using the techniques from this chapter. Study the differences.

### 1. Learning a New Skill

**Before:** "Teach me about photography."

**After:** "You are a photography instructor teaching a complete beginner who just bought their first camera (a basic DSLR). I have no experience with manual settings. Teach me the three most important settings to understand first (aperture, shutter speed, ISO). Explain each one using a real-world analogy, then give me one simple exercise to practice each setting. Keep the language simple and avoid technical jargon."

**Techniques used:** Role assignment, context, constraints ("avoid jargon"), output format (analogies plus exercises).

### 2. Writing a Difficult Message

**Before:** "Help me write a message to my boss."

**After:** "I need to ask my boss for a raise. I have been in my role for two years, my responsibilities have increased significantly since I started, and I recently led a project that brought in a major new client. Write a professional email requesting a salary review meeting. Keep the tone confident but not demanding. Under 200 words. Do not apologise for asking."

**Techniques used:** Context, task, rules, constraints ("do not apologise").

### 3. Making a Decision

**Before:** "Should I learn Python or JavaScript?"

**After:** "I am a 28-year-old marketing professional with no coding experience. I want to learn programming to automate repetitive tasks in my marketing work (data analysis, report generation, social media scheduling). I have about five hours per week to study. Compare Python and JavaScript for my specific situation. Consider: ease of learning for beginners, relevance to marketing tasks, job market value, and available free learning resources. Think through each factor step by step, then give me a clear recommendation."

**Techniques used:** Context, chain of thought ("think through each factor step by step"), output format (comparison by factor).

### 4. Getting Feedback on Your Work

**Before:** "Is this essay good?"

**After:** "You are a university writing instructor known for giving honest, constructive feedback. I am going to share a 500-word essay I wrote for a first-year English class. The assignment was to argue for or against social media's effect on mental health. Please evaluate it on four criteria: clarity of argument, strength of evidence, writing quality, and structure. For each criterion, give a score out of 10 and specific suggestions for improvement. Be direct. Do not soften your criticism."

**Techniques used:** Role assignment, output format (four criteria with scores), constraints ("do not soften your criticism").

### 5. Planning a Project

**Before:** "Help me plan a garden."

**After:** "I want to start a vegetable garden in my back garden. The space is approximately three metres by four metres. I live in the UK (Midlands), the area gets about six hours of sunlight per day, and the soil is clay-heavy. I am a complete beginner and I want to grow vegetables my family will actually eat: tomatoes, lettuce, herbs, and courgettes. Create a planting plan: what to plant where, when to plant each item, and what care each requires. Present the plan as a month-by-month calendar from March to September."

**Techniques used:** Context (location, sunlight, soil, family), task, output format (month-by-month calendar).

---

## Common Mistakes and How to Fix Them

### Mistake 1: Cramming Everything into One Prompt

Trying to get AI to do ten things in a single message usually produces mediocre results across the board. Instead, break the task into steps (Technique 7) and handle each one individually.

### Mistake 2: Being Vague About What You Want

"Make it better" is not useful feedback. Better how? More concise? More detailed? More formal? More casual? More persuasive? Be specific about the direction you want the revision to go.

### Mistake 3: Not Providing Context

The AI does not know who you are, what you do, what you have already tried, or what your constraints are unless you tell it. Context is not optional. It is the difference between generic output and personalised output.

### Mistake 4: Giving Up After One Bad Response

The first response is a starting point, not the finish line. If it is not right, refine it. Ask the AI what it misunderstood. Provide more context. Use the revision loop (Technique 5). Getting good results from AI is a conversation, not a single question.

### Mistake 5: Copying Someone Else's Prompt Without Understanding It

The internet is full of "magic prompts" that promise perfect results. Some of them work well, but only if they match your specific situation. Instead of copying prompts blindly, understand the principles behind them (context, task, rules, role, format) and build your own. A prompt you craft for your specific need will almost always outperform a generic "viral prompt" you found online.

### Mistake 6: Over-Complicating Your Prompts

More words do not automatically mean better results. A focused, clear prompt of three sentences often outperforms a rambling paragraph of ten sentences. Every sentence in your prompt should add useful information. If it does not add context, specify the task, or set a rule, it is noise.

---

## The Prompting Mindset

Everything in this chapter can be reduced to one idea: treat AI like a capable, willing collaborator who has never met you before and knows nothing about your specific situation.

A good collaborator can do excellent work for you. But only if you tell them what you need, give them the relevant background, explain your preferences, and provide feedback on their work. If you hand them a vague instruction and walk away, you will get a vague result. If you sit with them, explain the context, describe what success looks like, and iterate together, you will get something remarkable.

That is all prompt engineering is. It is the skill of being a good collaborator.

You do not need to memorise techniques. You do not need to study jargon. You just need to remember: the more clearly you communicate what you want, the better the result will be. Start with the formula (context, task, rules). Add techniques as they become useful. Refine through conversation. And give yourself permission to experiment, because the cost of trying a prompt that does not work is exactly zero.

---

## Chapter Summary

Here is what we covered, and what it means for you:

- **The prompt formula (context, task, rules) is the foundation of every effective AI interaction.** Context tells the AI who you are and what your situation is. Task tells it what to do. Rules tell it how to do it. Using all three consistently transforms generic output into personalised, useful responses.

- **Seven techniques improve AI output beyond the basics.** Role assignment shapes perspective. Few-shot prompting shows AI what you want through examples. Chain-of-thought prompting produces better reasoning. Output formatting makes responses immediately usable. The revision loop (draft, critique, revise) consistently produces the best results. Constraints prevent unwanted patterns. Breaking complex tasks into steps gives you control over the process.

- **Prompt engineering is a communication skill, not a technical skill.** If you can write a clear email or explain a task to a colleague, you can write effective prompts. The principles are the same: be clear, be specific, provide context, and give feedback.

- **The most effective AI users iterate.** They do not expect perfection on the first try. They draft, refine, redirect, and build through conversation. The back-and-forth is where the best results are created.

- **Start simple and add complexity as needed.** The formula alone will get you eighty percent of the way to excellent results. Add techniques one at a time as you discover situations where they help.

> **KEY FACT**
> Every effective prompt has three components: context (who you are and what your situation is), task (what you want the AI to do), and rules (format, tone, length, and constraints). Using all three consistently is the single biggest improvement most people can make to their AI interactions.

> **DID YOU KNOW?**
> You can ask AI to critique its own work and then rewrite it based on its own feedback. This revision loop (draft, critique, revise) consistently produces better output than any single prompt, no matter how carefully crafted. Professional AI users rely on this technique daily.

> **IN THE REAL WORLD**
> The difference between a beginner prompt and an expert prompt is rarely cleverness or technical knowledge. It is specificity. A beginner writes "help me with my resume." An experienced user writes "I am a marketing manager with seven years of experience applying for a director role at a tech startup. Review my resume and suggest three changes that would make it stronger for this specific role. Be direct." Same tool. Dramatically different result.

> **WATCH OUT**
> The internet is full of "magic prompts" that promise perfect results. Most of them work only in specific situations. Instead of copying prompts blindly, learn the principles behind them (context, task, rules, role, format, constraints) and build your own. A prompt you craft for your specific need will almost always outperform a generic template.

---

## Glossary

**Prompt Engineering:** The skill of communicating effectively with AI to get useful, high-quality results. Despite the technical-sounding name, it is fundamentally a communication skill based on clarity, specificity, and context.

**Context (in prompting):** Background information you provide so the AI can tailor its response. Includes who you are, what your situation is, what you already know, and any relevant details about your circumstances.

**Few-Shot Prompting:** A technique where you provide one or more examples of the kind of output you want before asking the AI to produce its own. The examples teach the AI your preferred style, format, or approach without you having to describe them in words.

**Chain-of-Thought Prompting:** Asking the AI to think through a problem step by step before giving its answer. This technique improves the quality of responses on complex questions that involve reasoning, analysis, or multi-step logic.

**Revision Loop:** A deliberate multi-round process where you first ask AI to produce a draft, then ask it to critique its own work, then ask it to revise based on the critique. Each cycle improves the output.

**Constraints:** Instructions that tell the AI what NOT to do. Constraints prevent common patterns, cliches, or default behaviours that do not match your needs. Examples: "Do not use jargon," "Do not exceed 200 words," "Do not start with a greeting."

**Output Format:** The structure you want the AI's response to take. Common formats include numbered lists, bullet points, tables, FAQs, step-by-step instructions, pros-and-cons lists, and specific word or sentence counts.

**Zero-Shot Prompting:** Giving AI a task without any examples. This is the default mode of interaction: you describe what you want and the AI relies on its training to produce a response. Most casual AI use is zero-shot prompting.

---

## Reflection

Think about the last time you tried to explain something to someone who did not understand what you wanted. Maybe it was a colleague, a contractor, a customer service representative, or a family member.

What made the communication break down? Was it a lack of context? Vague instructions? Assumptions you made about what they already knew?

Now think about how the same principles apply to AI. The AI does not know your situation, your preferences, or your constraints unless you tell it. The clearer you communicate, the better the result. This is true with people, and it is true with AI.

The next time you use an AI tool, try applying just one technique from this chapter. Use the formula. Assign a role. Give an example. Ask for step-by-step reasoning. See what changes.

---

*In Chapter 10, we turn honest. AI is powerful, but it is not perfect. It makes mistakes, invents facts, reproduces biases, and sometimes sounds completely confident while being completely wrong. Understanding what AI gets wrong is just as important as knowing what it gets right. Chapter 10 gives you the full picture.*
