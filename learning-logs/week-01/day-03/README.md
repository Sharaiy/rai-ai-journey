# Day 03 — Week 1 Consolidation & Establishing Blue Ocean Guardrails

**Date:** 2026-11-11
**Status:** Consolidation (not yet moving to Week 2)
**Focus:** Strengthening Week 1 foundations before starting OOP

---

## 🎯 Context for Today

Day 3 was carried out with two goals:
1. Ensure the Week 1 foundations (Python, Pandas, `np.where`, `try-except`, basic ML) are truly solid — not merely "feeling familiar".
2. Establish rules for using an AI agent (GLM via Cline/Roo Code) while staying inside the **Blue Ocean**: an AI Engineer with a Mechanical Engineering domain.

Key decision today: **not moving to Week 2 yet.** The reason is not a failed checkpoint, but because the closed-book test revealed several concepts still need consolidation.

---

## 🧠 Concept Corrections (Key Points)

Several initial understandings needed correction so they don't mislead in the future:

| Topic | Initial Understanding | Correction |
| :--- | :--- | :--- |
| `try-except` | "Filters junk data so accuracy improves" | **Wrong.** `try-except` is a safety net so the program doesn't crash. Data cleaning is Pandas' job (`dropna`, filtering, validation). Accuracy is driven by data quality + features + model, not error handling. |
| NumPy vs Pandas | "Two separate libraries" | **Not quite.** Pandas is built on top of NumPy. A DataFrame is a wrapper; inside it are NumPy arrays. This explains why `np.where` feels "odd" when NumPy isn't understood yet. |
| `train_test_split` | "To train ML with the data we submit" | **Incomplete.** The split separates training data and test data so the model **doesn't memorize**. Analogy: tensile test specimens from the same batch, but physically separated. Without a split → overfitting. |
| Overfitting vs Hallucination | "Both are AI weaknesses" | **Different.** Overfitting = classic ML, fails to generalize (high train, low test). Hallucination = LLM fabricating facts that sound convincing. Overfitting is relevant now; hallucination comes later (Week 5+). |

---

## 📊 Engineer-Style Data Handling (1,000 Rows)

Principle: data is not just a table of numbers, but **physical observations**. Every column must answer: unit, sensor, precision, operating condition, drift/calibration risk.

Agreed workflow:
1. **Profiling** — `describe()`, `isna()`, `dtypes`, duplicates, physical sanity checks (impossible temperatures, negative RPM, stuck sensors).
2. **Cleaning** — domain-based imputation (continuous temperature → interpolate; missing labels → drop), outliers checked first whether physical or sensor errors.
3. **EDA** — distribution per label, look for physically plausible patterns; suspect mislabeled data.
4. **Physics-based feature engineering** — `thermal_stress`, `vib_per_rpm`, `wear_index`, etc.
5. **Cross-validation** — 1,000 rows is too small for a single split; use `StratifiedKFold` and the **F1** metric, not accuracy (failure data is usually imbalanced).
6. **Interpretation** — check `feature_importances_`; if it doesn't make physical sense, suspect leakage or label noise.

**Traps to avoid:** normalizing before splitting, single split only, discarding outliers without physical checks, accuracy for imbalanced data, complex models for small data.

---

## 🗂️ Data Roadmap (Clarified)

| Phase | Data | Split | Status |
| :--- | :--- | :--- | :--- |
| Week 1–2 | **Synthetic** (self-generated, based on a wear model) | Random (`train_test_split`) | In progress |
| Week 3–4 | **NASA Bearing Dataset** | **Chronological** (`TimeSeriesSplit`) | Not started |
| Week 5+ | NASA Turbofan (CMAPSS), CWRU, etc. | Based on data characteristics | Not started |

Important note: NASA Bearing is **time-series**. A random split causes **leakage** (the model learns from the future). This differs from synthetic data, which can be shuffled safely.

Relevant portfolio data sources: NASA Bearing, CWRU Bearing, NASA CMAPSS, MIMII, UCI ML Repository.

---

## 🛡️ Blue Ocean Guardrails When Using AI Agents

Six rules agreed upon:

1. **Agent explains, it does not decide.** Every technical suggestion must be explainable in physical terms.
2. **70/30 ratio.** At least 70% of design decisions come from me; the agent at most 30% (boilerplate, refactor, documentation).
3. **Physical verification before commit.** Sanity-check physics, statistics, and leakage — not just "it runs without errors".
4. **Every project must have a Mechanical Engineering flavor.** No generic projects (Titanic, house price).
5. **Keep technical vocabulary sharp.** At least once a week, read mechanical engineering material and write notes without AI.
6. **Document the agent's role.** Record what I designed vs. what the agent helped with, and why suggestions were accepted or rejected.

**Working protocol (Predict → Write → Verify):**
- Predict the solution first without the agent (5–10 minutes).
- Write it myself; the agent only acts as a syntax translator.
- Verify line by line on small data.
- If something is wrong: analyze first, propose a hypothesis, then ask the mentor.

**Red flag:** if the agent is turned off and the exercise cannot be completed at all → I've become a passenger, not a pilot.

---

## ⚙️ AI Agent Usage (GLM)

- **Subscription required?** No. Free options: Cline with GLM-5.3-Flash (no API key needed), a free Zhipu AI API key (GLM-4.7-Flash / 4.5-Flash / 4.6V-Flash), or OpenRouter `:free` with rate limits.
- **Subscription** becomes relevant only when flagship models and large quotas are needed — not necessary at this stage.
- **Building a custom agent:** postponed. It requires OOP, APIs, and LLM/RAG understanding (Week 7+). For now, using an existing agent as a co-pilot is enough.

---

## ✅ Decisions Made Today

- [x] Postponed Week 2 until Week 1 consolidation is complete.
- [x] Established guardrails for AI agent usage.
- [x] Clarified the data roadmap (synthetic → NASA → advanced datasets).
- [x] Declined Coursera for now; focus on self-practice + mini projects.
- [x] Established consultation order: **mentor first for direction & concepts, agent later for implementation.**

---

## 🚧 What's Not Done (Honest)

- [ ] Closed-book retrieval practice: function + `try-except`, `np.where`, `train_test_split`.
- [ ] Mini capstone "Bearing Failure Prediction" (synthetic data → cleaning → features → split → Decision Tree → F1 evaluation).
- [ ] Writing `notes/week1_checkpoint.md` as evidence of understanding.
- [ ] Re-testing the 5 checkpoint questions without opening notes.

---

## 🎯 Next Steps

1. Complete the mini capstone today (target: 90 minutes, one working artifact).
2. Commit with a clear message and update the main README.
3. Re-test the checkpoint; if I pass ≥4/5 → mark **Week 1 ✅** and move to **Week 2: OOP for Mechanical Engineering** (`Material`, `Beam`, `@dataclass`).
4. If not yet passing → at most one additional consolidation day, focused on the remaining gaps.

---

## 💭 Reflection Note

Today felt heavy because awareness of the size of the gap increased. But a clearly visible gap is better than an unnoticed one. Blue Ocean is not about becoming the greatest AI Engineer, but about becoming an **AI Engineer who understands mechanical physics** — a pool with few competitors.

What must be preserved: consistency in finishing small things, not adding new terminology. Every project must have a clear **Technical Relevance**, so the Mechanical Engineering degree remains a foundation, not a memory.