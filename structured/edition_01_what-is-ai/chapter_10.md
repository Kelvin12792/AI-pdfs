# Chapter 10: What AI Gets Wrong

---

## Opening

For the past four chapters, you have been building a relationship with AI. You learned the tools. You had your first conversation. You mastered the art of prompting. By now, you have seen what AI can do, and if you have been following along and trying things yourself, some of those results probably impressed you.

Good. Now it is time for the honest conversation.

AI is powerful. It is also flawed. It makes mistakes. It invents facts. It reproduces biases that exist in the data it was trained on. It can sound perfectly confident while being completely, verifiably wrong. And unlike a human who might hesitate, hedge, or say "I am not sure," AI will often state a fabrication with the same calm authority it uses to state a proven truth.

Understanding these limitations does not diminish what AI can do. It makes you a smarter, safer, more effective user. A person who knows where the edge of a cliff is can walk closer to it without falling. A person who does not know the edge is there is in danger from the first step.

This chapter is your map of the cliff edges.

---

## Limitation 1: Hallucination -- When AI Invents Things That Do Not Exist

This is the limitation that has caused the most real-world damage, and the one every AI user must understand.

AI hallucination is the term for when an AI tool generates information that sounds authoritative and plausible but is entirely fabricated. It does not retrieve this false information from a database of lies. It constructs it, word by word, using the same process it uses to construct true statements. The AI does not know the difference between a real fact and a made-up one. It is predicting what words are most likely to come next, and sometimes the most likely-sounding sequence of words happens to describe something that does not exist.

Think of it this way. Imagine you ask someone for directions to a restaurant. Most people, if they do not know, will say "I am not sure." But imagine a person who is physically incapable of saying "I do not know." No matter what you ask, they give an answer. If they happen to know the way, the directions are excellent. If they do not know the way, they still give confident directions, complete with street names, landmarks, and estimated travel times. Everything sounds right. But you end up in an empty car park.

That is hallucination. AI cannot say "I do not know" in the way a human can. It generates a response, and that response may be accurate or it may be entirely invented, but the delivery is the same either way.

### Real Cases Where Hallucination Caused Serious Harm

This is not a theoretical risk. It has already caused documented, measurable harm in the real world.

**The New York Lawyers (2023).** Two attorneys in New York used ChatGPT to research legal precedents for a court filing. ChatGPT generated case citations that looked perfectly real: proper case names, correct formatting, plausible legal reasoning. The lawyers submitted these citations to a federal court. The problem: the cases did not exist. ChatGPT had invented them entirely. The judge described the fabricated content as "legal gibberish" and fined both lawyers five thousand dollars each. This case became the most widely reported example of AI hallucination and sent a shockwave through the legal profession.

But it was only the beginning.

**The MyPillow Case (2025).** Two attorneys representing a high-profile client used AI to prepare court filings that contained citations to cases that had never been decided by any court. A federal judge ordered each attorney to pay three thousand dollars in sanctions.

**The California Appellate Case (2025).** An attorney used ChatGPT and other AI tools to "enhance" his legal briefs. When the court investigated, it found that twenty-one of the twenty-three case quotations in his opening brief were fabricated. The court imposed a ten thousand dollar sanction and referred the attorney to the state bar for potential disciplinary action.

**The Deloitte Government Reports (2025).** The global consulting firm Deloitte submitted a report to the Australian government that contained hallucinated academic sources and a fabricated quote attributed to a federal court judgment. The report had cost the Australian government over four hundred thousand dollars. The following month, a separate Deloitte report for the Canadian government of Newfoundland and Labrador was found to contain at least four false citations to research papers that did not exist.

These are not edge cases. A database tracking AI hallucination incidents in legal proceedings alone now documents hundreds of cases worldwide. Before mid-2025, courts were seeing roughly two such cases per week. By the second half of 2025, the rate had accelerated to two or three cases per day.

### Why Hallucination Happens

Remember from Chapter 4 how AI works. It predicts the next most likely word based on patterns in its training data. When you ask it a factual question, it does not look up the answer in an encyclopedia. It generates a sequence of words that statistically fits the pattern of "what a correct answer to this kind of question usually looks like."

Most of the time, the pattern matches reality. But sometimes, the most likely-sounding pattern describes something that is not real. A legal citation that follows the correct format, uses plausible-sounding case names, and arrives at a reasonable-sounding conclusion can be entirely fabricated. It looks right because it follows the pattern of what real citations look like. The AI has no mechanism for checking whether the case actually exists.

Researchers at Anthropic published a study in 2025 examining the internal workings of AI models, and they identified specific circuits inside the model that are supposed to prevent the AI from answering when it does not have sufficient information. Hallucinations occur when these circuits fail, allowing the model to generate a confident-sounding answer even when it has no reliable basis for one.

One study found that over sixty percent of AI-generated citations were either broken or completely fabricated. These citations looked professional, used real-sounding publication names, and were often indistinguishable from valid references at a glance.

### The Danger of Confident Delivery

The most dangerous aspect of hallucination is not that AI makes things up. It is that it makes things up with the same tone, structure, and confidence it uses when stating verified facts. There is no warning light. No asterisk. No change in language. A hallucinated answer reads exactly like a factual one.

This is fundamentally different from human error. When a person is unsure, you can usually detect it: they pause, they hedge, they use phrases like "I think" or "if I remember correctly." AI does none of this by default. It presents everything with equal confidence, whether it is telling you the boiling point of water (correct) or citing a court case that was never decided (fabricated).

This is why the most important habit you can develop as an AI user is verification. Not for everything. Not for casual conversations or creative brainstorming. But for any factual claim that matters, for any statistic you plan to repeat, for any citation you plan to use, for any advice you plan to act on in areas like health, finance, or law, you must verify independently.

---

## Limitation 2: Bias -- When AI Reflects the World's Prejudices

AI learns from data. The data comes from the real world. The real world contains biases: racial bias, gender bias, age bias, cultural bias, socioeconomic bias, and many others. When AI trains on data that contains these biases, it absorbs them and reproduces them in its outputs.

This is not a bug in the programming. It is a consequence of the training process. If the training data contains patterns where certain groups are described in certain ways, the AI will learn those patterns and replicate them. The AI does not have opinions or prejudices. But it has learned statistical associations from data produced by a world that does.

### Documented Cases of AI Bias

**Hiring Discrimination.** Amazon built an AI recruiting tool designed to screen job applicants automatically. The system was trained on resumes submitted over a ten-year period. Because the technology industry has historically been male-dominated, the majority of those resumes came from men. The AI learned from this pattern and began penalising resumes that contained the word "women's" (as in "women's chess club captain") and downgrading graduates of all-women's colleges. Amazon tried to fix the system but ultimately abandoned it because they could not ensure it would not find new ways to discriminate.

**Age Discrimination in Hiring.** An AI recruitment system used by the education company iTutorGroup automatically rejected female applicants over the age of fifty-five and male applicants over the age of sixty. Over two hundred qualified candidates were disqualified based solely on their age. The U.S. Equal Employment Opportunity Commission filed a lawsuit, and the company settled for three hundred and sixty-five thousand dollars.

**Facial Recognition Errors.** MIT's Gender Shades project revealed that commercial facial recognition systems performed significantly worse on darker-skinned faces, particularly darker-skinned women. The error rates for lighter-skinned males were far lower than for darker-skinned females. Police departments using this technology have faced criticism for wrongful arrests that disproportionately affected people of colour.

**Healthcare Disparities.** AI diagnostic tools for skin conditions perform less accurately on darker skin because the training datasets contained predominantly images of lighter-skinned patients. AI systems trained mostly on data from male patients have been found to misdiagnose symptoms in women that present differently from the male patterns the system learned.

**The Resume Name Problem.** In bias testing conducted through 2025 and into 2026, AI resume screening tools showed measurably different selection rates based on the names on otherwise identical resumes. Research found systematic differences in how AI tools evaluated candidates from different racial and gender groups, even when qualifications were identical.

### Why Bias Is Hard to Fix

You might think the solution is simple: train AI on unbiased data. But there is no such thing as perfectly unbiased data about the real world, because the real world is not unbiased. Historical records reflect historical inequities. Language patterns reflect cultural assumptions. Photographs reflect who had access to cameras and who was photographed.

AI companies are actively working to reduce bias through better training data, filtering techniques, and evaluation methods. Progress is being made. But the problem is fundamental: any system that learns patterns from human-generated data will learn some human biases along with the useful patterns. Awareness of this limitation is essential for every AI user.

### What This Means for You

When you use AI, be aware that its responses can reflect biases you might not expect. If you ask AI to generate images of "a doctor," notice whether the images default to certain genders or ethnicities. If you ask AI to help screen job applicants, know that the outputs may systematically favour certain groups. If you ask AI for advice about people, careers, or cultures, consider whether the response might be shaped by biased patterns in the training data rather than by objective reality.

You do not need to distrust everything AI produces. But you should apply the same critical eye you would apply to any source of information that might carry implicit assumptions.

---

## Limitation 3: No Real Understanding

This is the most philosophically interesting limitation, and it has practical consequences for how you use AI.

AI does not understand what it is saying. It predicts the most likely next word in a sequence based on patterns. The result often looks like understanding. It can look remarkably like understanding. But the process behind it is fundamentally different from human comprehension.

There is a famous thought experiment that captures this distinction perfectly.

### The Translation Room

Imagine you are locked in a room. People slide pieces of paper under the door with Chinese characters written on them. You do not speak Chinese. You have never studied Chinese. But you have an enormous instruction manual, written in English, that tells you: "When you see this pattern of characters, write this pattern of characters in response."

You follow the instructions perfectly. The people outside the room are having a conversation with you in Chinese. From their perspective, the person in the room speaks fluent Chinese. From your perspective, you have no idea what any of the characters mean. You are matching patterns. You are producing correct responses. But you do not understand a single word.

This thought experiment was proposed by philosopher John Searle in 1980, and it remains one of the most influential arguments about AI and understanding. Modern AI operates similarly. It processes patterns and produces statistically appropriate responses. The responses are often useful, insightful, and even creative. But the system producing them does not understand the meaning of the words it generates any more than you understand Chinese in the thought experiment.

### What This Means in Practice

The lack of genuine understanding creates specific, predictable failure modes:

**AI has no common sense.** A human knows that water flows downhill, that you cannot fit an elephant in a shoebox, and that a person who says "I could eat a horse" is not actually planning to eat a horse. AI sometimes takes things literally that a human would recognise as figurative, or fails to apply basic physical intuitions that every human develops naturally through living in the physical world.

**AI cannot tell you about the real world right now.** Unless it has access to the internet (some tools do, some do not), AI has no knowledge of what is happening in the world at this moment. It cannot tell you whether it is raining outside, what the stock market did today, or whether a particular shop is open. It can generate plausible-sounding answers to these questions, but those answers come from pattern prediction, not from actual knowledge of current reality.

**AI can write poetry about love without ever having felt it.** It can describe the taste of chocolate without having tasted anything. It can explain grief without having lost anyone. The outputs can be moving, accurate, and deeply human-sounding, because they are based on patterns learned from millions of humans who did feel, taste, and grieve. But the system itself has no experience, no emotions, and no consciousness. It is producing the words that a person who had these experiences would probably write.

This does not mean AI is useless for these tasks. AI-generated writing about emotions can be beautiful and resonant. AI advice can be practical and helpful. But it is worth remembering that the system producing these outputs is doing sophisticated pattern matching, not drawing from lived experience.

---

## Limitation 4: The Struggle with Logic, Math, and Reasoning

AI is trained on language. It excels at tasks that are fundamentally linguistic: writing, summarising, translating, explaining. But it can struggle with tasks that require strict logical reasoning or precise mathematical calculation, because these tasks require a different kind of processing than "predict the next most likely word."

**Simple math errors.** AI can solve many math problems correctly, especially common ones it has seen many times in training. But it can make surprising errors on problems that a human with a calculator would get right every time. It might miscalculate a percentage, make an arithmetic error in a multi-step problem, or produce an answer that is close but not exact. This is improving rapidly with newer models, but it remains a known limitation.

**Logic puzzles.** AI can struggle with logic puzzles that require tracking multiple constraints simultaneously, especially novel ones it has not encountered in training. It might solve a well-known riddle perfectly (because it has seen the answer in training data) but fail on a slight variation of the same riddle that requires genuine logical reasoning rather than pattern recognition.

**Counting and spatial reasoning.** Asking AI to count the number of times a letter appears in a word, or to reason about spatial relationships between objects, can produce errors that seem absurd. These tasks feel trivially easy to humans but are genuinely difficult for a system that processes text as patterns of tokens rather than as representations of physical reality.

**The improving trajectory.** It is important to note that AI's reasoning abilities are improving significantly with each new generation of models. Tasks that tripped up AI models in 2023 may be handled correctly by models in 2026. But the underlying limitation remains: AI's reasoning is based on pattern prediction, not on the kind of structured logical processing that a human brain or a purpose-built calculator performs. Always verify mathematical results and logical conclusions independently when accuracy matters.

---

## Limitation 5: No Memory Across Conversations

You experienced this in Chapter 8, but it is worth understanding as a limitation with practical consequences.

Within a single conversation, AI remembers everything you have said. This creates the illusion of a relationship, of a system that knows you. But the moment you start a new conversation, that memory disappears completely. The AI does not remember your name, your preferences, your previous questions, or anything you discussed before.

Some AI tools are beginning to offer limited memory features that carry basic preferences across conversations. But in general, each conversation is independent. The AI that impressed you yesterday with its understanding of your situation will greet you today as a complete stranger.

This means that for ongoing projects, you need to re-establish context at the beginning of each new conversation. If you were working on a business plan yesterday and want to continue today, you need to provide the relevant details again. The AI will not remember where you left off.

This limitation also means that AI does not learn from you over time in the way a human mentor or colleague would. A human colleague who has worked with you for a year understands your style, your priorities, and your unspoken preferences. AI starts fresh every time. It is endlessly patient and always available, but it never develops the kind of accumulated understanding that comes from an ongoing relationship.

---

## Limitation 6: The Training Data Cutoff

AI models are trained on data up to a specific point in time. After that point, the model has no knowledge of what happened. It is like talking to someone who fell asleep on a particular date and just woke up. Everything that happened while they were asleep is invisible to them.

If you ask AI about events that occurred after its training data cutoff, it may tell you it does not have that information. Or it may hallucinate an answer based on patterns from events before the cutoff. For example, if you ask about the winner of an election that happened after the cutoff, it might predict the most likely winner based on pre-election polling in its training data, and present that prediction as fact.

Some AI tools have internet access that allows them to search for current information in real time. When using these tools, the cutoff is less of an issue for factual queries. But even with internet access, the AI's fundamental knowledge and reasoning patterns are shaped by the training data, not by what it retrieves in the moment.

---

## The First Pancake Principle

Here is a concept that will save you frustration and improve your results immediately.

When you make pancakes, the first one almost always turns out wrong. The pan is not hot enough, or too hot, or the batter is too thick, or you pour too much. The second pancake is better. By the third or fourth, you have found the right rhythm.

AI works the same way. The first response to your prompt is the first pancake. It is a starting point, not a finished product. The people who get the most value from AI are not the ones who get perfect results on the first try. They are the ones who treat the first response as a draft and then refine it.

This principle, which we touched on in Chapter 9, is especially important when it comes to AI limitations. If AI gives you a response that contains errors, that does not mean the tool is broken or useless. It means the first pancake came out wrong. Adjust your input. Provide more context. Ask the AI to double-check its work. Send it through the revision loop (draft, critique, revise). The quality of the output often improves dramatically between the first and third iterations.

The people who abandon AI after one bad result are making the same mistake as someone who throws away the entire bowl of pancake batter because the first one stuck to the pan.

---

## Your Fact-Checking Framework

Given everything you now know about AI's limitations, here is a practical three-step framework for verifying AI output when accuracy matters.

### Step 1: Assess the Stakes

Not everything needs to be fact-checked. If you asked AI to brainstorm birthday party ideas, the stakes are low. If you asked AI for medical information, legal advice, or financial data, the stakes are high.

Ask yourself: "If this information is wrong, what are the consequences?"

- **Low stakes:** Creative ideas, casual conversations, brainstorming, first drafts, general explanations of well-known concepts. Fact-checking is optional.
- **Medium stakes:** Work presentations, emails to clients, educational content, information you plan to share with others. Spot-check key claims.
- **High stakes:** Medical decisions, legal filings, financial planning, published research, anything with legal or professional consequences. Verify everything independently.

### Step 2: Check the Specifics

When AI provides specific claims (statistics, dates, names, quotes, citations), verify them independently. The more specific the claim, the more important it is to verify.

- **Statistics:** Search for the original source. Does the study exist? Does it say what AI claims it says?
- **Quotes:** Search for the exact quote. Did the person actually say it? Is the context accurate?
- **Citations:** If AI cites a book, article, or legal case, confirm it exists. This is the single most common hallucination type.
- **Recent events:** If the claim involves something that happened recently, check a reliable news source.

### Step 3: Use AI to Check Itself

This sounds counterintuitive, but it works. You can ask AI to verify its own claims:

- "Are you confident that statistic is accurate? Where does it come from?"
- "Can you double-check the citation you just gave me? Does that case actually exist?"
- "Review your previous response for any claims you are not certain about."

AI will often catch its own errors when directly prompted to look for them. This is not foolproof (the AI can hallucinate during its own fact-check too), but it catches a significant percentage of errors and is a useful first filter before you verify independently.

---

## When NOT to Trust AI Without Verification

Some domains require extra caution. In these areas, AI output should always be treated as a starting point for your own research, never as a final answer.

**Medical information.** AI can provide general health information that is often accurate and helpful. But it cannot diagnose you, it does not know your medical history, and it can be wrong about symptoms, drug interactions, and treatment options. Always consult a qualified healthcare professional for medical decisions.

**Legal advice.** As the hallucination cases in this chapter demonstrate, AI-generated legal information can be entirely fabricated. AI can help you understand legal concepts in general terms, but it should never be your sole source for legal decisions. Consult a qualified lawyer.

**Financial planning.** AI can explain financial concepts clearly and help you think through options. But it cannot account for your complete financial picture, it may generate inaccurate numbers, and it has no liability if its advice costs you money. Consult a qualified financial advisor for significant financial decisions.

**Academic and professional citations.** Never submit AI-generated citations without independently verifying that the sources exist and say what AI claims they say.

**Decisions that affect other people.** If your AI-assisted decision will significantly affect someone else (hiring, grading, evaluating, diagnosing), apply extra scrutiny. AI bias (Limitation 2) can silently influence these decisions in ways that are unfair to the people affected.

---

## The Error Reframe: Mistakes Are Clues, Not Failures

Here is the mindset shift that separates frustrated AI users from effective ones.

When AI gives you a wrong answer, that is not a failure of the tool. It is information about how to communicate better with the tool. The wrong answer is a clue.

If AI misunderstood your question, the clue is: your question was ambiguous. Rephrase it.

If AI gave you a generic answer, the clue is: you did not provide enough context. Add more detail.

If AI hallucinated a fact, the clue is: you asked for specific information that needs verification. Use the fact-checking framework.

If AI reproduced a bias, the clue is: the topic requires a critical eye. Evaluate the output through your own judgment, not just at face value.

Every error teaches you something about how AI processes your input and where its patterns break down. The more you learn from these errors, the better your prompts become, and the fewer errors you encounter over time.

This reframe also keeps AI in its proper place. AI is a tool. A powerful, versatile, often impressive tool. But it is a tool that you operate, evaluate, and ultimately take responsibility for. The output belongs to you the moment you use it. That means the verification is your responsibility, the judgment is your responsibility, and the decision about whether to trust or discard the output is your responsibility.

Understanding what AI gets wrong does not make AI less useful. It makes you more capable. You are now a user who knows where the edges are, what the risks look like, and how to navigate them. That makes you more effective than someone who trusts AI blindly, and more effective than someone who refuses to use it at all because they once got a wrong answer.

---

## Chapter Summary

Here is what we covered, and what it means for you:

- **AI hallucinates.** It invents facts, citations, statistics, and quotes with the same confidence it uses for accurate information. Hundreds of documented cases show real harm from hallucinated legal citations, fabricated academic sources, and invented statistics. Always verify factual claims when the stakes are high.

- **AI reflects biases from its training data.** Documented cases include hiring systems that discriminated by gender and age, facial recognition with higher error rates for darker-skinned faces, and healthcare tools that performed worse for underrepresented groups. Be aware that AI outputs can carry implicit biases.

- **AI does not genuinely understand what it says.** It predicts statistically likely word sequences. This produces results that look and feel like understanding but can break down with common sense, spatial reasoning, and novel situations.

- **AI struggles with precise math, logic, and counting.** While improving rapidly, AI's pattern-based reasoning can produce errors on tasks that require strict logical processing. Verify mathematical results and logical conclusions independently.

- **AI has no memory across conversations and a training data cutoff.** Each new conversation starts from zero. The AI's knowledge has a fixed endpoint, and information beyond that point may be unavailable or hallucinated.

- **Errors are clues, not failures.** Every wrong answer teaches you something about how to communicate more effectively with AI. The first pancake principle: treat early results as drafts and refine through iteration.

> **KEY FACT**
> AI hallucination is not a rare edge case. A database tracking AI-generated fabrications in legal proceedings alone documents hundreds of cases worldwide, with the rate accelerating to multiple incidents per day by 2025. Over sixty percent of AI-generated citations in one study were either broken or entirely fabricated. The single most important habit you can develop as an AI user is verifying factual claims independently.

> **DID YOU KNOW?**
> Amazon built an AI recruiting tool that taught itself to penalise resumes containing the word "women's" and to downgrade graduates of all-women's colleges, because it was trained on ten years of resumes from a male-dominated industry. Amazon tried to fix the bias but ultimately abandoned the entire project. AI does not have prejudices, but it learns patterns from data produced by a world that does.

> **IN THE REAL WORLD**
> In 2025, a court found that twenty-one of twenty-three case quotations in a lawyer's brief were fabricated by AI. The citations looked perfectly real: correct formatting, plausible case names, reasonable legal reasoning. But the cases had never been decided by any court. The attorney was fined ten thousand dollars and referred to the state bar. This is why verification is not optional for high-stakes use.

> **WATCH OUT**
> The most dangerous aspect of AI hallucination is not that AI makes things up. It is that it makes things up with exactly the same tone and confidence it uses for accurate information. There is no warning, no change in language, and no signal that the AI is uncertain. A hallucinated answer looks and reads exactly like a correct one. Assume nothing is verified until you have verified it yourself.

---

## Glossary

**Hallucination:** When AI generates information that sounds plausible and authoritative but is entirely fabricated. The term covers invented facts, fake citations, fabricated statistics, and any output that the AI presents as real but has no basis in reality.

**AI Bias:** Systematic patterns in AI output that unfairly favour or disadvantage certain groups of people. Bias enters AI through training data that reflects real-world inequities, historical patterns, and cultural assumptions.

**Training Data Cutoff:** The point in time beyond which an AI model has no knowledge. Events, publications, and developments after the cutoff are invisible to the model unless it has internet access.

**Verification:** The practice of independently confirming AI-generated claims through trusted sources. Essential for high-stakes use cases including medical, legal, financial, and academic applications.

**Common Sense Reasoning:** The type of intuitive understanding that humans develop naturally through living in the physical world. AI lacks this form of reasoning, which can lead to errors involving physical intuition, figurative language, and basic real-world knowledge.

**Pattern Matching:** The process by which AI identifies statistical regularities in data and uses them to generate responses. AI's strengths and many of its limitations both stem from this pattern-based approach.

**First Pancake Principle:** The concept that AI's first response to a prompt is rarely its best. Like the first pancake in a batch, it is a starting point. Iterative refinement through follow-up prompts consistently produces better results.

**Fact-Checking Framework:** A three-step process for verifying AI output: (1) assess the stakes, (2) check specific claims independently, (3) ask AI to review its own work for potential errors.

---

## Reflection

Think about a time when you received confident advice from a person who turned out to be wrong. Maybe it was directions that led you astray, a recommendation that did not work out, or information that you later discovered was inaccurate.

How did you respond? Did you stop trusting that person entirely? Or did you learn to verify their claims while still valuing their input?

AI is like that confident advisor. It is helpful far more often than it is wrong. But it is sometimes wrong, and it will never warn you when it is. The skill is not in avoiding AI. It is in knowing when to trust, when to verify, and when to override. That judgment is yours, and it always will be.

---

*In Chapter 11, we separate fact from fiction. AI is surrounded by myths: it will take everyone's jobs, it is about to become sentient, you need to be technical to use it, everyone else already understands it. Some of these myths have a grain of truth. Most do not. Chapter 11 takes the ten most common myths about AI and holds each one up to the evidence.*
