# PersonaGenerator

An advanced, production-grade Python engine designed for high-fidelity synthetic character engineering. Moving away from standard unweighted data arrays, this engine implements a **Persona-Centric Framework for AI Identity Engineering** to ensure deep psychological, operational, and demographic coherence across all output matrices.

---

## 🛠️ Framework Architecture

The generator is explicitly decoupled into independent modular components to allow localized optimization, targeted expansion, and clear behavioral auditiability:

1. **Identity Foundation Layer** (`names.py`, `surnames.py`, `physical_traits.py`)
   - Handles the demographic baseline. Incorporates a cascading biological sex and age matrix to ensure realistic hair, height, and feature distribution over random assignments.
2. **Psychological Core** (`fears_and_insecurities.py`, `skills_and_talents.py`, `sexual_preferences.py`)
   - Uses an algorithmic scoring engine mapped to Enneagram archetypes and personality temperaments. This creates dynamic behavioral vectors instead of flat random samplings.
3. **Contextual Environment Lens** (`culture_and_geography.py`, `careers_and_finance.py`)
   - Drives downstream variables deterministically via geographic and systemic anchors. Local accents, regional slang, educational backgrounds, and income ranges conform strictly to realistic regional models.
4. **Behavioral Alignment Layer** (`social_and_lifestyle.py`, `coachable_topics.py`)
   - Links attachment styles to relationship statuses, technical competencies, and tailored, forward-looking coaching inquiries satisfying International Coaching Federation (ICF) core standards.

---

## 🚀 Getting Started

### Project Structure
```text
PersonaGenerator/
├── PersonaGenerator.py          # Primary execution pipeline & orchestration engine
├── markdown_generator.py        # Structural markdown formatter & tracking token generator
├── md/                          # Default local output folder for generated bios
└── [Attribute Modules].py       # Explicit property matrices (Careers, Culture, Skills, etc.)
```

### Quick Execution
Ensure you have your environment paths set up properly within your project workspace directory (e.g., `C:\DIST\GitHub-Projects\PersonaGenerator`), then run the core file:

```bash
python.exe .\PersonaGenerator.py
```

### Sample Output Matrix
Every run generates an isolated, unique markdown profile stamped with a precise `Profile Tracking Token` for RAG parsing compatibility:

```markdown
# Persona: Christopher Vance
**Profile Tracking Token:** [ID-2026-08-20 00:15:32]

## Gender and Biological Sex
- **Age:** 42
- **Gender Identity:** cisgender man
- **Biological Sex:** male
- **Sexual Orientation:** heterosexual

## Personality Traits
- **Enneagram Type:** 8 - The Challenger
- **Temperament:** Conscientious
- **Sense of Humor:** Dark

## Coachable Topics
- How can you design your current role so that your impact expands while your baseline energy is actively restored?
- What would it look like to lean on the strengths of your team, allowing collaboration to replace your protective armor?
```

---

## 📊 Purpose & Downstream Applications

- **Grounding Context for LLMs:** Inject generated bio profiles into custom creative systems (e.g., instances running specialized configurations like `Heretic`) to ensure rock-solid character persistence.
- **RAG Pre-Loading:** Export structural markdown records directly to localized Vector Knowledge Bases to allow deep character cross-examination via RAG frameworks.
- **Agent Testing Boundaries:** Create diverse, distinct end-user proxies with predictable biases and conversational boundaries for software stress testing.
