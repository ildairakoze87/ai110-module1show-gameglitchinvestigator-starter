# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - A text box where you type a number between 1 and 100
  - A Submit Guess button to send your answer
  - A New Game button to restart
  - A Show Hint checkbox
  - It tells you how many attempts you have left( 6 for easy, 8 for normal and 5 for hard)


- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  -  it says the number of attenmpts allowed is 8 but its shows that attempts remaining are 7 before I even use my first attempt which is somehow not accurate.
  - 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Click New Game button | Game restarts and resets score/attempts | Button is less interactive and does not reliably restart the game | No console error shown, UI does not reset reliably |
| Enter 1 or 100 and submit | Hint should not say "go lower" after 1 or "go higher" after 100 | Hint message sometimes gives the opposite direction or invalid hint for edge values | No console error shown, hint logic is incorrect |
| Play until score reaches 0 | Score should stop at 0 and not go negative | Score can become negative after repeated guesses | No console error shown, score decrement logic allows negative values|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 - On this project i used ChatGPt and Claude. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
